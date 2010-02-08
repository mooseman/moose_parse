

#  pdparse.py  
#  Acknowledgement - This code is heavily inspired by (and some of it 
#  comes from) the public-domain Yeanpypa parser, done by Markus 
#  Bruckner. Very many thanks to Markus for creating Yeanpypa!  

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
        for rule, tok in zip(self.subrules, list(str.split(input)) ):  
           if tok == rule:             
              retval.append(input)            
           else: 
              pass 
           
        # Is the retval list the same length as the subrules list? 
        # If so, the parse succeeeded. If not, the parse failed.        
        if len(retval) == len(self.subrules):       
           print "Parse succeeded!" 
        else:    
           print "Parse failed."
        
        
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
        for rule, tok in zip(self.subrules, list(str.split(input)) ):               
           if tok in self.subrules: 
              retval.append(tok)                
           else: 
              pass  
              
        # If any rules matched, then the parse has succedded. 
        # Otherwise, the parse has failed.        
        if len(retval) > 0: 
           print "Parse succeeded." 
        else: 
           print "Parse failed"    
        
                                            
#  Create a simple grammar 
foo = AndRule("abc", "def")  
bar = OrRule("abc", "def") 

# This should fail. "abc" is not followed by "def" (or anything). 
foo.match("abc") 

#  This should succeed 
foo.match("abc def") 

# This should fail - tokens in the wrong order 
foo.match("def abc") 

# This should fail 
foo.match("abc deg") 

# This should succeed. 
bar.match("abc") 

# This should succeed. 
bar.match("def") 

# This should succeed. 
bar.match("abc def") 

# This should succeed. 
bar.match("abc foo") 

# This should succeed. 
bar.match("def foo") 

# This should succeed. 
bar.match("def foo test") 
      
      
      
      
      
      
      
              
