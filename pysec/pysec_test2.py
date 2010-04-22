

#  pysec_test.py 

from pysec import Parser, choice, quoted_chars, group_chars, \
   option_chars, digits, between, pair, spaces, match, \
   group, quoted_collection, sep_end_by

# HACK: json_choices is used to get around mutual recursion 
# A json value is one of text, number, mapping, and collection, 
# which we define later 
select_stmt = []

sql = choice(select_stmt) 

#text is any characters between quotes
text = quoted_chars("'", "'")

select = match('SELECT')

star = match('*')  

col = match(text) 

colstmt = choice(star, col) 

from_ = match('FROM')

tablestmt = text 

semi = match(';')  

# sql = select >> colstmt >> from_ >> tablestmt >> semi

#HACK: finish the work around mutual recursion
select_stmt.extend([select, colstmt, from_, tablestmt, semi])


############# testing ####################

print sql.parseString("SELECT 'city' FROM 'foo' ; ")



