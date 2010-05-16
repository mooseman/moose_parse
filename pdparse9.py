

#  pdparse9.py  

#  examples 

#  mystmt = Literal("test") + space + Literal("this")  
#  mygrammar = parse(mystmt, "test this")  


class test(object): 
   def match(self, arg):  
      return arg 
      
            
a = test() 

print a.match("foo") 


      







