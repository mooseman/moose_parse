

#  pdparse.py  
#  Acknowledgement - Most of this code comes from the public-domain 
#  Yeanpypa parser, done by Markus Bruckner. Very many thanks to 
#  Markus for creating Yeanpypa!  

#  Here, we see if it is possible to condense some of the Yeanpypa code 
#  down to a very small and simple parsing framework.  
#  This code is released to the public domain. 

import string 

class InputReader(object):    
    def __init__(self, string, ignore_white):
        
	self.__current_pos  = 0
	self.__stack        = []
        self.string       = string
        self.__ignore_white = ignore_white

    def getPos(self):        
        return self.__current_pos

    def skipWhite(self):        
        while (self.__current_pos < len(self.string) and self.string[self.__current_pos].isspace()):
            self.__current_pos += 1            
        
    def getString(self,length):        
        if self.__ignore_white:
            self.skipWhite()
        if self.__current_pos+length > len(self.string):
            raise EndOfStringException()
        start = self.__current_pos
        self.__current_pos += length
        return self.string[start:self.__current_pos]

    def getChar(self):        
        if self.__current_pos == len(self.string):
            raise EndOfStringException()
        if self.__ignore_white:
            self.skipWhite()
            logging.debug("Getting char at position %d" % self.__current_pos)
        logging.debug("Getting char at position %d" % self.__current_pos)
        char = self.string[self.__current_pos]
        self.__current_pos += 1
        return char

    def checkPoint(self):        
        self.__stack.append(self.__current_pos)

    def rollback(self):        
        if len(self.__stack) == 0:
            raise EmptyStackException()
        self.__current_pos = self.__stack[-1]
        self.__stack = self.__stack[:-1]

    def deleteCheckpoint(self):        
        if len(self.__stack) == 0:
            raise EmptyStackException()
        self.__stack = self.__stack[:-1]

    def fullyConsumed(self):        
        return len(self.string) == self.__current_pos

    def getIgnoreState(self):        
        return self.__ignore_white

    def setIgnoreState(self, state):        
        self.__ignore_white = state


# A parse result class 
class ParseResult(object):    
    def __init__(self, input_reader, token):        
        self.__input_reader = input_reader
        self.__token = token

    def full(self):        
        return self.__input_reader.fullyConsumed()

    def getTokens(self):        
        return self.__token


# A rule class for a grammar.  
class rule(object):    
   def match(InputReader): 
      pass 
      
   def __add__(self, second_rule):   
      return AndRule(self, second_rule)
      
   def __or__(self, second_rule):
      return OrRule(self, second_rule) 
      
      
#  Two or more rules matching directly after each other.        
class AndRule(rule):    
    def __init__(self, left_rule, right_rule):      
        self.subrules = [left_rule, right_rule]

    def __str__(self):        
        return "(%s)" % ' '.join(map(str, self.subrules))

    def __add__(self, right_rule):        
        self.subrules.append(right_rule)
        return self
    
    def match(self, InputReader):                
        retval = []
        for rule in self.subrules:
           result = rule.match(InputReader)
           if result != None:
              retval.append(result)            
           else: 
              pass    
        
        
# TODO: implement a greedy version of the OR rule (matches the longer match of the two)
class OrRule(rule):    
    def __init__(self, left_rule, right_rule):       
        self.subrules  = [left_rule, right_rule]

    def __str__(self):        
        return "(%s)" % ' | '.join(map(str, self.subrules))

    def __or__(self, right_rule):        
        self.subrules.append(right_rule)
        return self

    def match(self, InputReader):
        retval = []         
        for rule in self.subrules:
           result = rule.match(InputReader)                
           if result != None: 
              retval.append(result)                
           else: 
              pass 
        
              
              
#  Test the code.                
def parse(parser, string, ignore_white=True):    
    input_reader = InputReader(string, ignore_white)
    tokens = parser.match(input_reader)
    return ParseResult(input_reader, tokens)
      
      
#  Create a simple grammar 
foo = "abc" 
mygrammar = foo 


def parseit(grammar_name, input):
    result = parse(grammar_name, input)

    if result.full(): 
       print "Success!" 
    else: 
       print "Fail"  


#  Parse a few moves
parseit(mygrammar, "abc")
parseit(mygrammar, "def")


      
      
      
      
      
      
      
              
