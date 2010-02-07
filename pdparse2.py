

#  pdparse.py  
#  Acknowledgement - Most of this code comes from the public-domain 
#  Yeanpypa parser, done by Markus Bruckner. Very many thanks to 
#  Markus for creating Yeanpypa!  

#  Here, we see if it is possible to condense some of the Yeanpypa code 
#  down to a very small and simple parsing framework.  
#  This code is released to the public domain. 

import string 

            
#  Two or more rules matching directly after each other.        
class AndRule(object):    
    def __init__(self, left_rule, right_rule):      
        self.subrules = [left_rule, right_rule]

    def __add__(self, right_rule):        
        self.subrules.append(right_rule)
        return self
    
    def __str__(self):        
        return "(%s)" % ' '.join(map(str, self.subrules))
    
    def match(self, input):                
        retval = []
        for rule in self.subrules:
           if input == rule:             
              retval.append(result)            
           else: 
              pass    
        
        
# TODO: implement a greedy version of the OR rule (matches the longer match of the two)
class OrRule(object):    
    def __init__(self, left_rule, right_rule):       
        self.subrules  = [left_rule, right_rule]

    def __or__(self, right_rule):        
        self.subrules.append(right_rule)    
        return self 
        
    def __str__(self):        
        return "(%s)" % ' '.join(map(str, self.subrules))    

    def match(self, input):
        retval = []         
        for rule in self.subrules:
           if input == rule:            
              retval.append(result)                
           else: 
              pass 
        
                                  
#  Create a simple grammar 
foo = AndRule("abc", "def")  
bar = OrRule("abc", "def") 

print foo, bar 




      
      
      
      
      
      
      
              
