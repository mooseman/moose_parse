

#  moose_parse.py 

#  Just some simple code to play around with parsers 
#  Author: Andy Elvey 
#  This code is released to the public domain.  
#  TO DO -Need to be able to combine grammars in sequence 
#  so that we can have things like this - 
#  grammar = seq(parser1, parser2, parser3) 

#  A grammar has statements and tokens. Tokens need to have a "next" 
#  attribute which points to the next possible token. 
#  A token can have none, one, or more than one possible "next" token.  
 
class node(object): 
  def __init__(self): 
     self.name = self.next = None
     self.ndict = {}
    
#  Set a node's properties      
  def set(self, name, next): 
     self.name = name     
     self.next = next 
     self.ndict.update({ self.name:  [self.next] } )  
     
#  Get the properties of a node      
  def get(self, node): 
     if ndict.has_key(node): 
        return ndict[node] 
     
               
#  Grammar class 
#  A grammar will be made of a series of statements. 
#  A statement will be made of a series of nodes (tokens).  
class grammar(node): 
  def init(self): 
     self.grammar_dict = self.stmt_dict = self.node_dict = {} 
     
#  A statement method 
#  Stmt should be made of a series of nodes.  The last 
#  node will not have a "next" attribute.   
  def stmt(self, name, nodelist): 
     self.name = name 
     # The nodes which make up this statement 
     self.nodelist = nodelist 
     self.stmt_dict.update({self.name: self.nodelist })      

#  Add a node to a statement.       
  def add(self, stmtname, nodename, nextnode): 
     if grammar_dict.has_key(stmtname): 
        grammar_dict.update({stmtname: [nodename, nextnode] }) 
     else: 
        self.stmtname = stmtname 
        self.nodename = nodename 
        self.nextnode = nextnode 
        grammar_dict.update({self.stmtname: [self.nodename, self.nextnode] }) 
           
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
     
     








         
