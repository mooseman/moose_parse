

#  forward-declarations.py 
#  Experiment with a class which has forward declarations inside it. 
#  This is very handy for ding things like BNF grammars. 

#  Need to set __attr__ .  

# A function which has "placeholders" for parts of a grammar which are 
# calculated later.  
class lazy(object):  
   def __init__(self):  
      self.toks = {} 
 
   def eval(self): 
      pass 



class test(lazy): 
  def __init__(self): 
     self.mydict = {} 
     
  def add(self, attr): 
     if not hasattr(self): 
        self.setattr(attr) 
     else: 
        pass       
  
  
  
  def run(self):       
    self.foo = self.bar + self.baz     
    self.bar = self.splodge + self.splurge    
    self.baz = 58 
    self.splodge = 17 
    self.splurge = 34 
    # Everything has now been defined, so calculate the values of 
    # all attributes.  
    self.eval() 
         
  def display(self): 
    print self.foo, self.bar, self.baz 
     
     
#  Run the code 
a = test() 
a.run() 
a.display() 

      






