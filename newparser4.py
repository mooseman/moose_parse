
#  newparser4.py 

import string, itertools, curses.ascii 

# Some helper functions 
# alpha 
def alpha(ch): 
   if ch.isalpha(): 
      return 1
   else: 
      return 0 
    
# digit       
def digit(ch): 
   if ch.isdigit(): 
      return 1
   else: 
      return 0 
      
# alnum 
def alnum(ch): 
   if ch.isalnum(): 
      return 1 
   else: 
      return 0 
      
# space 
def space(ch): 
   if ch.isspace(): 
      return 1 
   else:
      return 0 
      
# punctuation 
def punct(str):
   count = 0 
   mylen = len(str) 
    
   for ch in str:  
      if curses.ascii.ispunct(ch):   
         count += 1
      else: 
         pass 
         
   if count == mylen: 
      return 1
   else: 
      return 0             
      
# A "literal". Look for a given string. 
def lit(mylit, str):       
   if str == mylit: 
      return 1 
   else: 
      return 0       
        
         
def any_p(func, args ): 
   count = 0 
   for x in args:  
      if func(x): 
         count += 1                
      else: 
         pass 
   if count > 0: 
      return 1 
   else: 
      return 0       
      
         
print any_p(digit, "foo3") 
print any_p(digit, "bar")          
         
         
         
         
# Test 
print alpha("abc") 
print alpha("abc1")
print alnum("abc1") 
print alnum("abc$")  
print digit("123")
print digit("123a") 
print space("   ")
print space("   a") 
print punct("%^&*") 
print punct("%^&*a") 
print lit("def", "def") 
print lit("def", "defg") 


# Now, we can start to do the main parse functions. Things like 
# any, none, and, or, not, in, not_in, sepby and so on. 
# After that, we can look at "tokens" (words). That is when we can 
# also look at doing a "next" method or function, for the next token.  






'''
class parser(object): 
   def __init__(self): 
      pass  ''' 
      
      
      
   

      
      
      

