

#  generic_sequence.py 
#  A generic sequence class which uses a dictionary to store the 
#  sequence.  
#  Author:  Andy Elvey 
#  This code is released to the public domain.  

#  TO DO - Look at adding separate "add" methods for tuples, 
#  strings, csv data. That data would be converted to a list, 
#  then added to the dict.  


import itertools 

class myseq(object): 
   def init(self): 
       self.datadict = {} 
       self.nextkey = 0
       
   def add(self, data):
      for k, v in enumerate(data, self.nextkey): 
         self.datadict[k] = v  
      self.nextkey += len(data)  
      
   def display(self): 
      print self.datadict 
      

# Run the code 
a = myseq() 

a.init() 

a.add(["foo", "bar", "baz"]) 

a.add(["The", "quick", "brown", "fox", "jumps", "over", "the", \
     "lazy", "dog"]) 
     
a.add([12, 42, 387, 424, 96, 2317, 5178])      
     
a.add(["Mary", "had", "a", "little", "lamb", "its", "fleece",  \
      "was", "white", "as", "snow"])    
     
a.display() 


                          
                 
