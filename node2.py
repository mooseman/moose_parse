

 
class node(object): 
  def __init__(self, data, next=None): 
     self.data = data 
     self.next = next 
              
  def display(self): 
     print self.data, self.next  
     
     
#  Run the code 
a = node('proc', 'print') 
b = node('print', 'data') 
c = node('data', '=') 
d = node('=', 'foo') 

a.display()
b.display()
c.display()
d.display()

    
