

#  moose_parse.py

#  This parser is basically a somewhat stripped-down version of the 
#  Yeanpypa parser by Markus Brueckner. Very many thanks to Markus 
#  for doing Yeanpypa.  
#  The main differences: Some of the leading underscores have been 
#  removed from variable names. Some code comments have been removed.  
#  Some error-checking code has been removed.   

#  This code is released to the public domain.  
#  "Share and enjoy..."  ;)     



import logging

class InputReader(object):
   def __init__(self, string, ignore_white):
      self.current_pos  = 0 
      self.stack        = []
      self.string       = string
      self.ignore_white = ignore_white   

   def getPos(self):
      return self.current_pos 
      
   def skipWhite(self): 
      while (self.current_pos < len(self.string) and self.string[self.current_pos].isspace()):
         self.current_pos += 1    

   def getString(self,length):
      if self.ignore_white:
         self.skipWhite()
      if self.current_pos+length > len(self.string):
         raise EndOfStringException()
      # Start of the string is at the current position    
      start = self.current_pos
      self.current_pos += length
      return self.string[start:self.current_pos] 

   def getChar(self):
      if self.current_pos == len(self.string):
         raise EndOfStringException()
      if self.ignore_white:
         self.skipWhite()
         logging.debug("Getting char at position %d" % self.current_pos)
      logging.debug("Getting char at position %d" % self.current_pos)
      # We return the char at the current position 
      char = self.string[self.current_pos]
      # Advance the pointer by one 
      self.current_pos += 1
      return char 

   def checkPoint(self):
      self.stack.append(self.current_pos) 

   def rollback(self):
      if len(self.stack) == 0:
         raise EmptyStackException()
      self.current_pos = self.stack[-1]
      self.stack = self.stack[:-1] 

   def deleteCheckpoint(self):
      if len(self.stack) == 0:
         pass    
         #raise EmptyStackException()
      self.stack = self.stack[:-1] 

   def fullyConsumed(self):
      return len(self.string) == self.current_pos 
      
   def getIgnoreState(self):
      return self.ignore_white
      
   def setIgnoreState(self, state):
      self.ignore_white = state         


class ParseException():  
   def __init__(self): 
      return None 

class EndOfStringException():  
   def __init__(self): 
      return None 



class ParseResult(object): 
   def __init__(self, input_reader, token): 
      self.input_reader = input_reader
      self.token = token

   def full(self):
      return self.input_reader.fullyConsumed() 
      
   def getTokens(self): 
      return self.token   



class Rule(object): 
  action     = None
  hide_token = False

  def match(input_reader): 
     pass 
     
  def __add__(self, second_rule): 
     return AndRule(self, second_rule)
     
  def __or__(self, second_rule):
     return OrRule(self, second_rule)      

  def setaction(self, action): 
     self.action = action 
     return self 
     
  def callAction(self, param): 
     if self.action:
        if isinstance(param, list):
           return self.action(param)
        else:
           return self.action([param])
     else:
        return param  
  
  def hide(self):
     self.hide_token = True
     return self 
    
  def returnToken(self, token):
     if self.hide_token:
        return None
     else:
        return token    
    
    
    
class Literal(Rule):
     def __init__(self, string):
        self.string = string
        
     def __str__(self):
        return "\"%s\"" % self.string 
        
     def match(self, input_reader): 
        # Save the position of the pointer 
        input_reader.checkPoint()
        try:
            string = input_reader.getString(len(self.string))
            # The input does not match our string 
            if string != self.string: 
                # Roll back the parse 
                input_reader.rollback()
                #raise ParseException()
                #raise ParseException("Expected '%s' at position %d. Got '%s'" % (self.string, input_reader.getPos(), string))
        except EndOfStringException: 
            # End of string reached without a match 
            input_reader.rollback()
            #raise ParseException()
            #raise ParseException("Expected '%s' at end of string" % self.string)
        # We have a successful match, so delete the checkpoint.  
        input_reader.deleteCheckpoint()
        logging.debug("Matched \"%s\"" % self)
        # Return the string and call its action (if it has one).  
        return self.returnToken(self.callAction([self.string]))
   
                 
        
class AndRule(Rule):    
     def __init__(self, left_rule, right_rule): 
        self.subrules = [left_rule, right_rule] 
        
     def __str__(self):
        return "(%s)" % ' '.join(map(str, self.subrules))    
        
     def __add__(self, right_rule):
        self.subrules.append(right_rule)
        return self 
        
     def match(self, input_reader): 
        retval = []
        try:
            input_reader.checkPoint()
            for rule in self.subrules:
                result = rule.match(input_reader)
                if result != None:
                    retval.append(result)
            input_reader.deleteCheckpoint()
        except ParseException:
            input_reader.rollback()
            raise
        return self.returnToken(self.callAction(retval))   
    


class OrRule(Rule):    
     def __init__(self, left_rule, right_rule): 
        self.subrules = [left_rule, right_rule] 
        
     def __str__(self):
        return "(%s)" % ' | '.join(map(str, self.subrules))    
        
     def __or__(self, right_rule):
        self.subrules.append(right_rule)
        return self 
        
     def match(self, input_reader): 
        input_reader.checkPoint()
        for rule in self.subrules:
            try:
                rule_match = rule.match(input_reader)
                input_reader.deleteCheckpoint()
                return self.returnToken(self.callAction(rule_match))
            except ParseException:
                pass
        input_reader.rollback()
        raise ParseException("None of the subrules of %s matched." % str(self))

    
def parse(parser, string, ignore_white=True): 
    input_reader = InputReader(string, ignore_white)
    tokens = parser.match(input_reader)
    return ParseResult(input_reader, tokens)


#  A function to parse input
def parseit(grammar_name, input):
    result = parse(grammar_name, input)

    if result.full(): 
       print "Success!" 
    else: 
       print "Fail"  




