
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








'''
class parser(object): 
   def __init__(self): 
      pass  ''' 
      
      
      
   

      
      
      

