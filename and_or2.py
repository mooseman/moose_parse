

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
            raise EmptyStackException()
      self.stack = self.stack[:-1] 

   def fullyConsumed(self):
      return len(self.string) == self.current_pos 
      
   def getIgnoreState(self):
      return self.ignore_white
      
   def setIgnoreState(self, state):
      self.ignore_white = state         



class Rule(object): 
  def match(input_reader): 
     pass 
     
  def __add__(self, second_rule): 
     return AndRule(self, second_rule)
     
  def __or__(self, second_rule):
     return OrRule(self, second_rule)      

  def setaction(self, action): 
     self.action = action 
     return self 
     
    
class AndRule(Rule):    
     def __init__(self, left_rule, right_rule): 
        self.subrules = [left_rule, right_rule] 
        
     def __str__(self):
        return "(%s)" % ' '.join(map(str, self.subrules))    
        
     def __add__(self, right_rule):
        self.__subrules.append(right_rule)
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

    
#  TO DO - need to add a parse class. This would take foo objects as 
#  input, and scan them according to a grammar.   

#  Test the code 
a = foo("test") 

b = foo(" this") 

c = a + b 

d = a | b 

print c, d  

 



   
        
                 


