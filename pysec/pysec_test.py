

#  pysec_test.py 

from pysec import Parser, choice, quoted_chars, group_chars, \
   option_chars, digits, between, pair, spaces, match, \
   quoted_collection, sep_end_by

#HACK: json_choices is used to get around mutual recursion 
#a json is value is one of text, number, mapping, and collection, which we define later 
json_choices = []
json         = choice(json_choices)

#text is any characters between quotes
text         = quoted_chars("'", "'")

#sort of like the regular expression -?[0-9]+(\.[0-9]+)?
#in case you're unfamiliar with monads, "parser >> Parser.lift(func)" means "pass the parsed value into func but give me a new Parser back"
number       = group_chars([option_chars(["-"]), digits, option_chars([".", digits])]) >> Parser.lift(float)

#quoted_collection(start, space, inner, joiner, end) means "a list of inner separated by joiner surrounded by start and end"
#also, we have to put a lot of spaces in there since JSON allows lot of optional whitespace
joiner       = between(spaces, match(","), spaces)
mapping_pair = pair(text, spaces & match(":") & spaces & json)
collection   = quoted_collection("[", spaces, json,         joiner, "]") >> Parser.lift(list)
mapping      = quoted_collection("{", spaces, mapping_pair, joiner, "}") >> Parser.lift(dict)

#HACK: finish the work around mutual recursion
json_choices.extend([text, number, mapping, collection])


############# simplified CSV ########################

def line(cell):
    return sep_end_by(cell, match(","))

def csv(cell):
    return sep_end_by(line(cell), match("\n"))

############# testing ####################

print json.parseString("{'a' : -1.0, 'b' : 2.0, 'z' : {'c' : [1.0, [2.0, [3.0]]]}}")
print csv(number).parseString("1,2,3\n4,5,6")
print csv(json).parseString("{'a' : 'A'},[1, 2, 3],'zzz'\n-1.0,2.0,-3.0")





