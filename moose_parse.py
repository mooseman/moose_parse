

#  moose_parse.py 

#  Just some simple code to play around with parsers 
#  Author: Andy Elvey 
#  This code is released to the public domain.  
#  TO DO -Need to be able to combine grammars in sequence 
#  so that we can have things like this - 

#  Note - By far the easiest way to organise the grammar would be to 
#  code it from the "bottom up", like yeanpypa. This is the reverse of
#  how BNF grammars are displayed, but it is much easier to implement. 


#  grammar = oneormore(stmt) 
#  stmt = oneof(stmt1, stmt2, stmt3, stmt4) 
#  stmt1 = seq([token1, token2, token3, token4, token5, token6]) 
#  stmt2 = seq([token1, token2, token3]) 
#  token1 = oneof(foo, bar) 
#  token2 = oneof(["this", "is", "just", "a", "test"])  


#  A grammar has statements and tokens. Tokens need to have a "next" 
#  attribute which points to the next possible token. 
#  A token can have none, one, or more than one possible "next" token.  
 
class node(object): 
  def __init__(self): 
     self.name = self.next = None
     self.ndict = {}
    
#  Set a node's properties 
#  A node can have a name, a type (e.g. token, operator, identifier), 
#  a value and a "next node" attribute.       
  def set(self, name, type, value, next): 
     self.name = name     
     self.type = type 
     self.value = value 
     self.next = node()  
     self.ndict.update({ self.name: [self.type, self.value, self.next] } )  
     
#  Get the properties of a node      
  def get(self, node): 
     if ndict.has_key(node): 
        return ndict[node] 
     
     
#  A statement class. Statements will be made up of a series of nodes.     
class stmt(node): 
  def init(self): 
     self.stmt_dict = {} 

  def add(self, node): 
     self.node = node()      
     self.stmt_dict.update({ self.node.name: [self.node.type, 
          self.node.value, self.node.next] }) 
     
  def display(self): 
     print self.stmt_dict       
     
               
#  Grammar class 
#  A grammar will be made of a series of statements. 
#  A statement will be made of a series of nodes (tokens).  
class grammar(stmt): 
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
     
     








         
