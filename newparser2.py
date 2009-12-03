

#  newparser.py 

import string, curses, curses.ascii  

class parser(object): 
   def init(self): 
      # The parser type 
      self.type = self.prevtype = None 
      self.pos = 0 
      self.result = ""  
      # A list to hold a sequence of parse results 
      self.seq = [] 
      self.count = 0
      self.alpha = self.digit = self.alnum = self.punct \
        = self.upper = self.lower = self.ws = 0 
        
   def chartypecount(self, ch): 
      self.ch = ch 
      if self.ch.isdigit():       
         self.type = "d"                   
      elif self.ch.isalpha(): 
         self.type = "a"
      elif self.ch.isspace(): 
         self.type = "s"             
      elif curses.ascii.ispunct(self.ch):          
         self.type = "p"                      
      else: 
         pass 
      
      #  Do stuff here 
      if self.type == self.prevtype: 
            self.count = self.count + 1
      elif self.type != self.prevtype and self.prevtype != None:
            self.count = 1 
            self.seq.append(str(self.count) + self.prevtype) 
      elif self.type != self.prevtype and self.prevtype == None:      
            self.count = 1 
            self.seq.append(str(self.count) + self.type)       
                           
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


  
            
                                 

