

#  moose_parse.py 

#  Just some simple code to play around with parsers 
#  Author: Andy Elvey 
#  This code is released to the public domain.  


def parse(data, stuff): 
   for x in data: 
     if x == stuff: 
         print "Found!" 
     else: 
         pass           
         
# A parser to parse two things (like parens, or whatever) 
# separated by other stuff.  
def paren(data, first, last):    
   if first in data and last in data and \
      data.index(last) >= (data.index(first) + len(first) +1): 
      print "Got it!" 
   else: 
      print "Sorry" 


#  Create a separate "action class" for a parser 
class action(): 
  def found(self): 
     print "Found many" 
  def not_found(self): 
     print "Did not find many" 
          
#  Inherit the action class into our parser 
class many(object, action): 
   def parse(self, data, stuff): 
      self.data = data 
      self.stuff = stuff    
      if self.data.count(self.stuff) >= 2: 
         self.found()  
      else: 
         self.not_found() 
                               
         
# Run the code 
parse("aabb1nnaa1bvd1fa", "1") 

paren("aaabbhgjfcc", "aaa", "cc") 

paren("aaabb", "aaa", "bb") 

paren("aaaxbb", "aaa", "bb") 
             
                     
a = many()                      
a.parse("aabfdaa", "a") 

a.parse("abcde", "z") 

a.parse("abcde", "a") 

a.parse("aaabgfdaaaedsrfaaaghytrf", "aaa") 








         
