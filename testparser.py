

#  testparser.py  
#  Test the moose_parse parser.  

from moose_parse import * 

grammar = Literal("Just") + Literal("a") + Literal("test")  

grammar2 = Literal("foo") | Literal("bar") | Literal("baz") 


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


