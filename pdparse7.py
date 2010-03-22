

#  pdparse.py  
#  Acknowledgement - This code is heavily inspired by (and some of it 
#  comes from) the public-domain Yeanpypa parser, done by Markus 
#  Bruckner. Very many thanks to Markus for creating Yeanpypa!  

#  Here, we see if it is possible to condense some of the Yeanpypa code 
#  down to a very small and simple parsing framework.  
#  This code is released to the public domain. 

import string, curses, curses.ascii, itertools   

# A literal string.
def literal(stuff): 
   type = "literal" 
   return "\"%s\"" % stuff  
   
def alpha(stuff): 
   type = "alpha" 
   if stuff.isalpha(): 
      return stuff 
   else: 
      return "Failed - not alpha"    
            
def alnum(stuff): 
   type = "alnum"    
   if stuff.isalnum(): 
      return stuff 
   else: 
      return "Failed - not alnum"    
         
def digit(stuff): 
   type = "digit" 
   if "int" in str(stuff.__class__): 
      return stuff 
   elif stuff.isdigit(): 
      return stuff 
   else: 
      return "Failed - not digit"    

def punct(stuff): 
   type = "punct" 
   for x in stuff: 
      if curses.ascii.ispunct(x): 
         return stuff 
      else: 
         return "Failed - not punct"    

def space(stuff): 
   type = "space" 
   if stuff.isspace(): 
      return stuff 
   else: 
      return "Failed - not space"    


# Get the type of a parser  
def gettype(parser): 
   return parser.type 
   

# For each of these parsers, match the stored pattern type against the 
# type of each of the input tokens.  

def one_or_more(type, stuff): 
   count=0 
   
   for x in stuff: 
      if x.type == type: 
         count += 1 
      else: 
         pass    
   
   
def zero_or_more(stuff): 
   pass 

def zero_or_one(stuff): 
   pass 

def n_or_more(n, stuff): 
   pass 

def n_to_m(n, m, stuff): 
   pass 
   
   
# Now - need a parser class. This takes a pattern to match against, 
# and some input to parse.  
   


# Test the code 
print literal("foo") 
print alpha("foo") 
print alnum("foo") 
print digit("foo") 
print digit(123) 
print punct("foo") 
print punct("@#$%&") 
print space("     ") 
print space("foo") 









              
