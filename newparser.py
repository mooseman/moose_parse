

#  newparser.py 

import string, curses, curses.ascii  

class parser(object): 
   def init(self): 
      # The parser type 
      self.type = self.prevtype = None 
      self.pos = 0 
      self.result = None 
      # A list to hold a sequence of parse results 
      self.seq = [] 
      self.count = 0
      self.alpha = self.digit = self.alnum = self.punct \
        = self.upper = self.lower = self.ws = 0 
        
   def chartypecount(self, ch): 
      self.ch = ch 
      if self.ch.isdigit():             
         self.prevtype = self.type 
         self.type = "d"
         if self.type == self.prevtype: 
            self.count += 1
         elif self.type != self.prevtype:
            self.count = 1 
            self.seq.append(str(self.digit) + self.prevtype)    
         
         
         self.punct = self.upper = self.lower = self.ws = 0          
         self.digit = self.digit + 1          
         self.pos += 1 
         
                  
      elif self.ch.isalpha(): 
         self.prevtype = self.type 
         self.type = "a"
         
         
         
         self.punct = self.digit = self.ws = 0  
         self.alpha = self.alpha + 1        
         self.pos += 1
         if self.type == self.prevtype: 
            pass 
         else: 
            self.seq.append(str(self.alpha)+ self.type) 
            
      elif self.ch.isspace(): 
         self.prevtype = self.type 
         self.type = "s"
         self.punct = self.alpha = self.upper = self.lower \
            = self.digit = 0  
         self.ws = self.ws + 1 
         self.pos += 1
         if self.type == self.prevtype: 
            pass 
         else: 
            self.seq.append(str(self.ws) + self.type)
         
      elif curses.ascii.ispunct(self.ch):          
         self.prevtype = self.type 
         self.type = "p"
         self.alpha = self.upper = self.lower = self.digit = self.ws = 0 
         self.punct = self.punct + 1 
         self.pos += 1         
         if self.type == self.prevtype: 
            pass 
         else: 
            self.seq.append(str(self.punct) + self.type)
            
      else: 
         pass 
         
   # A "match" function. Use this to match (say) x letters followed by 
   # y digits, and so on.          
   # For example, "4a5d" would be fouir letters followed by 5 digits. 
   def match(self, mytype):                                              
      self.mytype = mytype             
    
   def parse(self, input): 
      for ch in input: 
         self.chartypecount(ch) 
                      
   def display(self): 
      print self.seq                       
                      
   def result(self):           
         if self.mytype: 
            print "Success" 
         else: 
            print "Fail" 
  
# Test the parser 
a = parser()
a.init()
a.match("5a5d") 
a.parse("moose45678") 
a.display() 
# a.result() 


  
            
                                 

