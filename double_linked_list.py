
# double_linked_list.py
# An attempt at a double-linked list class.
# Author: Andy Elvey
# This code is released to the public domain.
# "Share and enjoy......"  :)
 
 
class dll(object):
   def init(self):
      self.prev = self.address = self.next = 0
      self.nodedict = {}
 
   def add(self, data):
      self.data = data
      self.address = self.next
      self.next += 1
      self.nodedict.update( {self.address: (self.prev , self.next, self.data ) })
      self.prev = self.address
            
   def display(self):
      print self.nodedict
      
# Run the code
a = dll()
 
a.init()
 
a.add("foo bar baz")
 
a.add( (12, 43, 54, 68) )
 
a.add("Ayyyye..... LUX-ury!")
 
a.display()
 
 
 
