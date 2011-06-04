

#  testparser.py  
#  Test the moose_parse parser.  

# This code is released to the public domain.  
#  "Share and enjoy..."  :)  


from moose_parse2 import * 


grammar = Literal("Just") + Literal("a") + Literal("test")  

grammar2 = Literal("foo") | Literal("bar") | Literal("baz") 

procname = (Literal("print") | Literal("summary") )

grammar3 = Literal("proc") + procname + Literal("data") + \
   Literal("=") + Literal("test") + Literal(";") 

grammar4 = OneOrMore(alnum) 
#grammar4 = letters  


# Try to parse a file 
myfile = open("mygrammar.txt", 'r') 


#  A function to parse input
def parseit(grammar_name, input):

    result = parse(grammar_name, input)

    if result.full(): 
       print "Success!" 
    else: 
       print "Fail"  


#  Parse a few tokens
parseit(grammar, "Just a test")

parseit(grammar2, "foo")

parseit(grammar2, "bar")

# This should fail 
parseit(grammar, "Just test a")

# ... and so should this 
parseit(grammar2, "bark")

parseit(grammar3, "proc print data=test;") 

parseit(grammar3, "proc summary data=test;") 

# This works 
parseit(grammar3, "".join(['proc summary data=test;'])) 

parseit(grammar3, "".join(['proc print data=test;'])) 

# This works!  
# The read() method reads the whole file in one go.
# The key is to make sure you include the 
# strip() function. Without it, the parse fails.  
# I think this works because it removes the EOF charcter 
# ( Ctrl-D ).  
#parseit(grammar3, "".join(myfile.read().strip() )) 
parseit(grammar3, myfile.read().strip() )

parseit(grammar4, "abc") 

myfile.close() 

