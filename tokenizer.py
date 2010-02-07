

#  tokenizer.py  
#  A simple tokenizer.  
#  To start with, we try to tokenize a small part of SQL - 
#  the SELECT clause. This gives us a manageable number of keywords 
#  and operators to deal with.  

#  This code is released to the public domain. 
#  "Share and enjoy...."  ;)  

import string 

#  Parse the tokens. Check if they are in the grammatically-correct 
#  order. 
def parse(toklist): 
   keywordlist = ["SELECT", "FROM", "WHERE", "AND", "OR", 
     "NOT", "IN", "CASE", "THEN", "ELSE", "END", "AS"] 
   
   oplist = ["+", "-", "*", "/", "<", ">", "<=", ">=", "=", 
     "eq", "ne", "lt", "gt", "le", "ge"]    
          
   if (word in keywordlist) or (word in oplist): 
      return word 
   else:        
      return "Word not found!" 
      
           
#  Tokenizer
def tokenize(stuff): 
   toklist = [] 
   tokens = str.split(stuff)
   for tok in tokens: 
      toklist.append(tok) 
   print toklist 
      
      
tokenize("SELECT * FROM MYTABLE WHERE CITY = 'SYDNEY' ; ")       
      
      
      
      
      
           
     





