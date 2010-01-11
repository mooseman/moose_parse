

# stack.py 

# A very simple class using a list as a stack. 
# This can be used for (for example) keeping track of parens, 
# brackets and so on.  

# This code is released to the public domain.  


class stack(object): 
   def init(self): 
      self.stack = [] 
      
   def push(self, stuff): 
      self.stack.append(stuff) 
      
   def pop(self): 
      self.stack.pop() 
      
   def display(self): 
      print self.stack 
      
#  Test the code
a = stack() 
a.init() 
a.push("abc")
a.push("123")
a.push("foo")
a.push("bar") 
a.pop()
a.pop()
a.display() 



      
            
            



