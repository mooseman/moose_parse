

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


# A parser to parse things in sequence 
def parse_seq(data, first, next): 
    if (first and next) in data and data.index(next) > data.index(first): 
        print "Next followed first"
    else:
        print "Nope... sorry!" 


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
             

# Try the "many" parser class                      
a = many()                      
a.parse("aabfdaa", "a") 

a.parse("abcde", "z") 

a.parse("abcde", "a") 

a.parse("aaabgfdaaaedsrfaaaghytrf", "aaa") 


#  Parse sequences 
parse_seq("aaaabbbrgr", "bbb", "rgr")

parse_seq("aa23aabb67brgr", "23", "67") 

parse_seq("The quick brown fox", "The", "fox")  

parse_seq("The quick brown fox", "fox", "quick")  

parse_seq([12, 23, 45, 32], "23, 45", "32" ) 







         
