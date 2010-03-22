

#  pdparse.py  
#  Acknowledgement - This code is heavily inspired by (and some of it 
#  comes from) the public-domain Yeanpypa parser, done by Markus 
#  Bruckner. Very many thanks to Markus for creating Yeanpypa!  

#  Here, we see if it is possible to condense some of the Yeanpypa code 
#  down to a very small and simple parsing framework.  
#  This code is released to the public domain. 

import string 

# Parse a literal string.
class Literal(object):   
    def __init__(self, string):  
        self.string = string 

    def __str__(self):       
        return "\"%s\"" % self.string 

    def match(self, input):               
        if input == self.string:
           #return self.string
           print "Literal parse succeeded!"
        else:
           print "Parse failed."
           
    def __add__(self, other):
        return AndRule([self.string, other.string])
       
    def __or__(self, other):
        return OrRule([self.string, other.string])

            
class Keyword(object): 
    def __init__(self, keyword): 
        self.keyword = keyword 
        
    def save(self): 
        if not self.hasattr(self.keyword): 
           self.setattr(self.keyword, self.keyword) 
        else: 
           pass        
               
    def __str__(self): 
        return "\"%s\"" % self.string             
        
    def match(self, input): 
        if input == self.string: 
           return self.string 
        else: 
           return "Parse failed." 
           
                  
#  Two or more rules matching directly after each other.        
class AndRule(object):    
    def __init__(self, rule_list):      
        self.rule_list = rule_list

    def __add__(self, rule):        
        self.rule_list.append(rule)
        return self
    
    def __str__(self):        
        return "(%s)" % ' '.join(map(str, self.rule_list))
    
    def match(self, input):                
        retval = []
        for rule, tok in zip(self.rule_list, list(str.split(input)) ):  
           if tok == rule:             
              retval.append(input)            
           else: 
              pass 
           
        # Is the retval list the same length as the subrules list? 
        # If so, the parse succeeeded. If not, the parse failed.        
        if len(retval) == len(self.rule_list):       
           print "Parse succeeded!" 
        else:    
           print "Parse failed."
        #return self.returnToken(self.callAction(retval))
        
        
# TODO: implement a greedy version of the OR rule (matches the longer match of the two)
class OrRule(object):    
    def __init__(self, rule_list):       
        self.rule_list = rule_list

    def __or__(self, rule):        
        self.rule_list.append(rule)    
        return self 
        
    def __str__(self):        
        return "(%s)" % ' '.join(map(str, self.rule_list))    

    def match(self, input):
        retval = []       
        for rule, tok in zip(self.rule_list, list(str.split(input)) ):               
           if tok in self.rule_list: 
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
        
         
class parser(object): 
    def __init__(self): 
       self.ruledict = {} 
                  
    def display(self): 
       print self.ruledict         
        
                                                            
#  Create a simple grammar       
test = Literal("try") + Literal("this") 
test.match("try this") 

foo = Literal("first") | Literal("second") 
foo.match("second")       
      
      
      
      
      
      
              
