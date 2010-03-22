

#  pdparse.py  
#  Acknowledgement - This code is heavily inspired by (and some of it 
#  comes from) the public-domain Yeanpypa parser, done by Markus 
#  Bruckner. Very many thanks to Markus for creating Yeanpypa!  

#  Here, we see if it is possible to condense some of the Yeanpypa code 
#  down to a very small and simple parsing framework.  
#  This code is released to the public domain. 

import string 


class Rule(object):    
    action     = None
    hide_token = False

    def match(input_reader):        
        pass

    def __add__(self, second_rule):        
        return AndRule(self, second_rule)

    def __or__(self, second_rule):        
        return OrRule(self, second_rule)

    def setAction(self, action):        
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

    def match(self, input):                
        if input == self.string:
           return self.string 
        else: 
           return "Parse failed."  

            
#  Two or more rules matching directly after each other.        
class AndRule(Rule):    
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
        #return self.returnToken(self.callAction(retval))
        
        
# TODO: implement a greedy version of the OR rule (matches the longer match of the two)
class OrRule(Rule):    
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
              #return self.returnToken(self.callAction(tok))             
           else: 
              pass  
              
        # If any rules matched, then the parse has succedded. 
        # Otherwise, the parse has failed.        
        if len(retval) > 0: 
           print "Parse succeeded." 
        else: 
           print "Parse failed"    
        
                                            
#  Create a simple grammar 
foo = Literal("abc") 
bar = Literal("def")  

baz = AndRule(foo, bar)  
test = OrRule(foo, bar) 

# This should fail. "abc" is not followed by "def" (or anything). 
baz.match("abc") 

# This should succeed 
baz.match("abc def") 

# This should succeed.   
baz.match("abc def ghi") 

# This should fail - tokens in the wrong order 
baz.match("def abc") 

# This should fail 
baz.match("abc deg") 

# This should succeed. 
test.match("abc") 

# This should succeed. 
test.match("def") 

# This should succeed. 
test.match("abc def") 

# This should succeed. 
test.match("abc foo") 

# This should succeed. 
test.match("def foo") 

# This should succeed. 
test.match("def foo test") 
      
      
      
      
      
      
      
              
