


import itertools 


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
      for x in self.templist: 
         if x.isspace(): 
            self.templist.remove(x) 
            
      if all(x.isdigit() for x in self.templist): 
         x = int(x) 
      else: 
         pass 
      for k, v in enumerate(self.templist, self.nextkey): 
         self.dict[k] = v  
      self.nextkey += len(data)          

   def display(self): 
      print self.dict 


# Run the code 
a = add() 

a.init() 

a.listproc(["mary", "had", "a", "little", "lamb", "its", \
     "fleece", "was", "white", "as", "snow"]) 
     
a.tupleproc( ("this", 42, "is", "436", "just", 3.857, "a", \
      "little", 3245, "test") ) 
      
a.stringproc("mary had a little lamb, its fleece was white as snow", " ") 

a.display() 

