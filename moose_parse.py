

#  moose_parse.py 

#  Just some simple code to play around with parsers 
#  Author: Andy Elvey 
#  This code is released to the public domain.  
#  TO DO -Need to be able to combine grammars in sequence 
#  so that we can have things like this - 
#  grammar = seq(parser1, parser2, parser3) 
 



def parse(data, stuff): 
   if stuff in data:  
     print "Found!" 
   else: 
     print "Not found" 
         
# A parser to parse two things (like parens, or whatever) 
# separated by other stuff.  
def paren(data, first, last):    
   if first in data and last in data and \
      data.index(last) >= (data.index(first) + len(first) +1): 
      print "Got it!" 
   else: 
      print "Sorry" 


#  An "add" class to process data when it is used in 
#  the parse_seq function 
#  NOTE - this is how the "all" and "any" functions are used - 
#  a[3] = "little" 
#  >>> all(x.isalpha() for x in a[3])
#  True
#  >>> any(x.isdigit() for x in a[3])
#  False


class add(object): 
   def init(self): 
      self.dict = {} 
      self.nextkey = 0 
            
   def listproc(self, data): 
      for k, v in enumerate(data, self.nextkey): 
         self.dict[k] = v  
      self.nextkey += len(data) 
      
   def tupleproc(self, data): 
      for k, v in enumerate(data, self.nextkey): 
         self.dict[k] = v  
      self.nextkey += len(data)       
 
   def stringproc(self, data, splitchar): 
      self.templist = data.split(splitchar) 
      if all(x.isdigit() for x in self.templist): 
         x = int(x) 
      else: 
         pass 
      for k, v in enumerate(self.templist, self.nextkey): 
         self.dict[k] = v  
      self.nextkey += len(data)          
           
   def display(self): 
      print self.dict 
           
           
                  
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



#  A class which overloads the ">" operator. 
class test(object):
   def __gt__(self, other):
      if other == "foo":
         print "found!" 
      else: 
         print "not found" 
         
   def seq(self, data, first, next): 
    if (first and next) in data and data.index(next) > data.index(first): 
        print "Next followed first"
    else:
        print "Next did not follow first"  
        
                     
#  Test the class 
a = test()
a.__gt__("foo")   #  "found!" 
a.__gt__("bar")   #  "not found" 

a > "foo"         #  "found!" 
a > "bar"         #  "not found"  

a.seq("Mary had a great big moose", "great", "big") 
a.seq("Mary had a great big moose", "big", "great") 











         
