

 
class node(object): 
  def __init__(self, data, next=None): 
     self.data = data 
     self.next = next 
         
#  Set a node's properties 
#  A node can have a name, a type (e.g. token, operator, identifier), 
#  a value and a "next node" attribute.       
  def set(self, name, type, value, next): 
     self.name = name     
     self.type = type 
     self.value = value 
     self.next = next   
     self.ndict.update({ self.name: [self.type, self.value, self.next] } )  
     
#  Get the properties of a node      
  def get(self, node): 
     if ndict.has_key(node): 
        return ndict[node] 
     
  def display(self): 
     print self.ndict 
     
     
#  Run the code 
a = node() 
a.set('foo', 'token', 123, 'bar') 
a.set('bar', 'token', "Some text", 'baz') 
a.set('baz', 'token', ("A", "nice", "little", "tuple"), None) 
a.display() 
 
     
