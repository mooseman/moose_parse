

#  test.py 


class foo(object):  
  def init(self): 
    self.mydict = {} 
    
  def add(self, key, data): 
    self.key = key
    self.data = data 
    self.mydict.update({ self.key: [self.data] })  
              
  def display(self): 
    print self.mydict 
    
    
class bar(foo): 
  foo() 
  
  
#  Test the code 
a = bar() 
a.init()
a.add("hi there", 123)
a.add("hello", 456)
a.display() 

  
  
      
         
  
  
  
  
  
  


