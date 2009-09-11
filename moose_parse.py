

#  moose_parse.py 

#  Just some simple code to play around with parsers 
#  Author: Andy Elvey 
#  This code is released to the public domain.  
#  TO DO -Need to be able to combine grammars in sequence 
#  so that we can have things like this - 
#  grammar = seq(parser1, parser2, parser3) 

#  A grammar has statements and tokens. Tokens need to have a "next" 
#  attribute which points to the next possible token. 
#  A token can have none, one, or more than one "next" token.  
 
class node(object): 
  def __init__(self): 
     self.name = self.type = self.next = None
     
       
#  Grammar class 
class grammar(node): 
  def init(self): 
     self.gdict = {} 

#  Add a node or statement      
  def add(self, name, type):
     self.name = name   
     self.type = type 
     
#  Action method, to be used with nodes, statements.      
  def action(self): 
     pass       
     
#  Run the grammar      
  def run(self): 
     for stmt in self.gdict: 
        stmt.action()           
     
#  Display the grammar      
  def display(self): 
     print self.gdict 
     
     
#  Test the code 
a = grammar() 
a.init() 
     
     








         
