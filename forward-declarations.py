

#  forward-declarations.py 
#  Experiment with a class which has forward declarations inside it. 
#  This is very handy for ding things like BNF grammars. 

#  Need to set __attr__ .  

class test(object): 
  
  def run(self):       
    self.foo = self.bar + self.baz     
    self.bar = self.splodge + self.splurge    
    self.baz = 58 
    self.splodge = 17 
    self.splurge = 34 
         
  def display(self): 
    print self.foo, self.bar, self.baz 
     
     
#  Run the code 
a = test() 
a.run() 
a.display() 

      






