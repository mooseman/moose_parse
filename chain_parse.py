


#  chain_parse.py 
#  Use the chain itertool to parse sequences. 

#  Note - all(iterable) is equivalent to - 
#  def all(iterable):
#      for element in iterable:
#          if not element:
#              return False
#      return True

#  >>> a = "ggg"
#  >>> b = all(x == "g" for x in a)
#  >>> b
#  True
#  >>> b = all(x == "z" for x in a)
#  >>> b
#  False
#  >>>

#  >>> a = "123foo"
#  >>> b = any(x.isdigit() for x in a) 
#  >>> b
#  True

#  >>> a = all(x < 40 for x in [12,23,37])
#  >>> a
#  True

#  >>> a = "foo123bar"
#  >>> b = (x.isalpha() for x in a)
#  >>> b
#  <generator object <genexpr> at 0xb7e2eb94>
#  >>> b.next()
#  True


import itertools, curses.ascii  



def myparse(data, stuff): 
   for x in data: 
     if x == stuff: 
         print "Found!" 
     else: 
         pass       


class parser(object): 
   def init(self): 
      self.result = False 
      
   def chain(self, *parsers): 
      self.myparser = itertools.chain(*parsers)      
      
   def parse(self, data, parser): 
      self.result = itertools.chain(parser, data) 
      self.result = parser(data) 
      if parser:  
         print "True"       
      else: 
         print "False" 
         
                     
#  Run the code 
a = parser() 

a.init() 

a.parse("foo123bar8767baz", myparse) 


                     






