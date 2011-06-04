

#  moose_parse.py

#  This parser is basically a somewhat stripped-down version of the 
#  public domain Yeanpypa parser by Markus Brueckner. Very many thanks 
#  to Markus for doing Yeanpypa.  
#  The main differences: Some of the leading underscores have been 
#  removed from variable names. Some code comments have been removed.  
#  The exception-handling code has been removed. This is just my own 
#  preference - I like to be hands-on with the parser code, without 
#  exceptions code getting in the way and cluttering things up. 

#  This code is released to the public domain.  
#  "Share and enjoy..."  ;)     



import logging

class InputReader(object):
   def __init__(self, string, ignore_white):
      self.current_pos  = 0 
      self.stack        = []
      self.string       = string
      self.length       = len(self.string)  
      self.ignore_white = ignore_white   

   def getPos(self):
      return self.current_pos 
      
   def skipWhite(self): 
      while (self.current_pos < (self.length) and self.string[self.current_pos].isspace()):
         self.current_pos += 1    

   def getString(self):
      if self.ignore_white:
         self.skipWhite()
      if self.current_pos+self.length > (self.length):
         raise EndOfStringException()
      # Start of the string is at the current position    
      start = self.current_pos
      self.current_pos += self.length
      return self.string[start:self.current_pos] 

   def getChar(self):
      if self.current_pos == len(self.string):
         raise EndOfStringException()
      if self.ignore_white:
         self.skipWhite()
         logging.debug("Getting char at position %d" % self.current_pos)
      logging.debug("Getting char at position %d" % self.current_pos)
      # We return the char at the current position 
      char = self.string[self.current_pos]
      # Advance the pointer by one 
      self.current_pos += 1
      return char 

   def checkPoint(self):
      self.stack.append(self.current_pos) 

   def rollback(self):
      if len(self.stack) == 0:
         raise EmptyStackException()
      self.current_pos = self.stack[-1]
      self.stack = self.stack[:-1] 

   def deleteCheckpoint(self):
      if len(self.stack) == 0:
         pass    
         #raise EmptyStackException()
      self.stack = self.stack[:-1] 

   def fullyConsumed(self):
      return len(self.string) == self.current_pos 
      
   def getIgnoreState(self):
      return self.ignore_white
      
   def setIgnoreState(self, state):
      self.ignore_white = state         


class ParseException():  
   def __init__(self): 
      return None 

class EndOfStringException():  
   def __init__(self): 
      return None 



class ParseResult(object): 
   def __init__(self, input_reader, token): 
      self.input_reader = input_reader
      self.token = token

   def full(self):
      return self.input_reader.fullyConsumed() 
      
   def getTokens(self): 
      return self.token   



class Rule(object): 
  action     = None
  hide_token = False

  def match(input_reader): 
     pass 
     
  def __add__(self, second_rule): 
     return AndRule(self, second_rule)
     
  def __or__(self, second_rule):
     return OrRule(self, second_rule)      

  def setaction(self, action): 
     self.action = action 
     return self 
     
  def callAction(self, param): 
     if self.action:
        if isinstance(param, list):
           return self.action(param)
        else:
           return self.action([param])
     else:
        return param  
  
  def hide(self):
     self.hide_token = True
     return self 
    
  def returnToken(self, token):
     if self.hide_token:
        return None
     else:
        return token    
    
    
    
class Literal(Rule):
     def __init__(self, string):
        self.string = string
        
     def __str__(self):
        return "\"%s\"" % self.string 
        
     def match(self, input_reader): 
        # Save the position of the pointer 
        input_reader.checkPoint()
        try:
            string = input_reader.getString()
            # The input does not match our string 
            if string != self.string: 
                # Roll back the parse 
                input_reader.rollback()
                #raise ParseException()
                #raise ParseException("Expected '%s' at position %d. Got '%s'" % (self.string, input_reader.getPos(), string))
        except EndOfStringException: 
            # End of string reached without a match 
            input_reader.rollback()
            #raise ParseException()
            #raise ParseException("Expected '%s' at end of string" % self.string)
        # We have a successful match, so delete the checkpoint.  
        input_reader.deleteCheckpoint()
        logging.debug("Matched \"%s\"" % self)
        # Return the string and call its action (if it has one).  
        return self.returnToken(self.callAction([self.string]))
   
  
class AnyOf(Rule):
    """
    A class to match chars from a charset. The class matches exactly one of the chars from
    the given charset. Whitespaces are matched depending on the setting of the input reader.
    Note that if the input reader is set to ignore whitespaces, they will not be matched even
    if the charset contains a whitespace character.
    """
    def __init__(self, set):
        """
        Initialize the object with a given set.

        @param set: the charset this rule should match
        @type  set: str
        """
        self.set = set

    def __str__(self):
        """
        Return a human readable representation of the rule.

        @return: A string describing the rule
        """
        return "AnyOf(%s)" % self.set

    def match(self, input_reader):
        """
        Match a character from the input. Depending on the setting of the input reader, the next
        character ist matched directly or the next non-whitespace character is matched.

        @param input_reader: The input to read from.
        @type  input_reader: InputReader
        @return: The matched character
        """
        input_reader.checkPoint()
        char = ''
        try:
            char = input_reader.getChar()
            if not (char in self.set):
                input_reader.rollback()
                raise ParseException("Expected char from: [%s] at %d" % (self.set, input_reader.getPos()))
        except EndOfStringException:
            input_reader.rollback()
            raise ParseException("Expected char from: [%s] at %d" % (self.set, input_reader.getPos()))
        input_reader.deleteCheckpoint()
        logging.debug("Matched %s" % char)
        return self.returnToken(self.callAction([char]))


class NoneOf(Rule):
    """
    Match if the next character is NOT in the given set.
    """
    def __init__(self, set):
        """
        Initialize the rule with the given set.

        @param set: The char set the rule should NOT match on.
        @type  set: str
        """
        self.set = set
        
    def __str__(self):
        """
        Return a human readable representation of the rule.

        @return A string describing the rule
        """
        return "NoneOf(%s)" % self.set

    def match(self, input_reader):
        """
        Match the rule against the input.

        @param input_reader: The input reader to read the next character from.
        @type  input_reader: InputReader
        @return: The matched char not in the set.
        """
        input_reader.checkPoint()
        char = ''
        try:
            char = input_reader.getChar()
            if char in self.set:
                input_reader.rollback()
                raise ParseException("Expected char not from: [%s] at %d" % (self.set, input_reader.getPos()))
        except EndOfStringException:
            input_reader.rollback()
            raise ParseException("Expected char not from: [%s] at %d" % (self.set, input_reader.getPos()))
        input_reader.deleteCheckpoint()
        logging.debug("Matched %s" % char)
        return self.returnToken(self.callAction([char]))
  
                        
class AndRule(Rule):    
     def __init__(self, left_rule, right_rule): 
        self.subrules = [left_rule, right_rule] 
        
     def __str__(self):
        return "(%s)" % ' '.join(map(str, self.subrules))    
        
     def __add__(self, right_rule):
        self.subrules.append(right_rule)
        return self 
        
     def match(self, input_reader): 
        retval = []
        try:
            input_reader.checkPoint()
            for rule in self.subrules:
                result = rule.match(input_reader)
                if result != None:
                    retval.append(result)
            input_reader.deleteCheckpoint()
        except ParseException:
            input_reader.rollback()
            #raise
        return self.returnToken(self.callAction(retval))   
    

class OrRule(Rule):    
     def __init__(self, left_rule, right_rule): 
        self.subrules = [left_rule, right_rule] 
        
     def __str__(self):
        return "(%s)" % ' | '.join(map(str, self.subrules))    
        
     def __or__(self, right_rule):
        self.subrules.append(right_rule)
        return self 
        
     def match(self, input_reader): 
        retval = [] 
        try: 
           input_reader.checkPoint()
           for rule in self.subrules:
               result = rule.match(input_reader) 
               if result != None: 
                  retval.append(result) 
           input_reader.deleteCheckpoint()
        except ParseException:
            input_reader.rollback()
            #raise
        return self.returnToken(self.callAction(retval))   
           
           
class Optional(Rule):
    
    #This rule matches its subrule optionally once. If the subrule does
    #not match, the Optional() rule matches anyway.    
    def __init__(self, rule):
        #Initialize the rule with a subrule.
        #@param rule: The rule to match optionally
        #@type  rule: Rule        
        self.rule = rule

    def __str__(self):
        #Return a string representation of this rule.
        #@return: a human readable representation of this rule.        
        return "[ %s ]" % str(self.rule)

    def match(self, input_reader):
        #Match this rule against the input.
        #@param input_reader: The input reader to read from.
        #@type  input_reader: InputReader
        #@return A list of token matched by the subrule (or None, if none)        
        try:
            rule_match = self.rule.match(input_reader)
            logging.debug("Matched %s" % self)
            return self.returnToken(self.callAction(rule_match))
        except ParseException:
            pass
            
            
class OneOrMore(Rule):
    #Match a rule once or more. This rule matches its subrule at least
    #once or as often as possible.    
    def __init__(self, string):
        #Initialize the rule with the appropriate subrule.
        #@param rule: The subrule to match.
        #@type  rule: Rule        
        self.string = string

    def __str__(self):
        #Return a human-readable representation of the rule.
        #@return: A string describing this rule.
        return "\"%s\"" % self.string 
        
    def match(self, input_reader): 
        # Save the position of the pointer 
        input_reader.checkPoint()
        try:
            string = input_reader.getString()
            # The input does not match our string 
            if string != self.string: 
                # Roll back the parse 
                input_reader.rollback()
                #raise ParseException()
                #raise ParseException("Expected '%s' at position %d. Got '%s'" % (self.string, input_reader.getPos(), string))
        except EndOfStringException: 
            # End of string reached without a match 
            input_reader.rollback()
            #raise ParseException()
            #raise ParseException("Expected '%s' at end of string" % self.string)
        # We have a successful match, so delete the checkpoint.  
        input_reader.deleteCheckpoint()
        logging.debug("Matched \"%s\"" % self)
        # Return the string and call its action (if it has one).  
        return self.returnToken(self.callAction([self.string]))    
        
    
                
        
class Combine(Rule):
    """
    Pseudo rule that recursivly combines all of it's children into one token.
    This rule is useful if the token of a group of subrules should be combined
    to form one string.
    """
    def __init__(self, rule):
        """
        Initialize the rule with a subrule.  The token generated by
        the subrule are recursivly combined into one string.

        @param rule: The subrule to combine.
        @type  rule: Rule
        """
        self.rule = rule

    def __str__(self):
        """
        Return a human-readable description of the rule.

        @return: A string describing this rule.
        """
        return "Combine(%s)" % str(self.rule)

    def combine(self, token):
        """
        Recursivly combine all token into a single one. This is an internal helper that
        recursivly combines a list of lists (or strings) into one string.

        @param token: the token list to combine into one string.
        @type  token: list or str
        """
        if token==None:
            return None
        #retval = ''
        retval=[]
        for tok in token:
            retval.append(tok)            
        return retval

    def match(self, input_reader):
        """
        Match this rule against the input. The rule matches the input
        against its subrule and combines the resulting token into a
        string.

        @param input_reader: The input reader to read from.
        @type  input_reader: InputReader
        @return: A string combining all the token generated by the subrule.
        """
        retval = self.combine(self.rule.match(input_reader))
        return self.returnToken(self.callAction(retval))


def Word(param):
    """
    a shortcut for Combine(MatchWhite(OneOrMore(AnyOf(string)))) or
    Combine(MatchWhite(OneOrMore(param))) (depending on the type of
    param). See there for further details.
    """
    if isinstance(param, str):
        return Combine(MatchWhite(OneOrMore(AnyOf(param))))
    else:
        return Combine(MatchWhite(OneOrMore(param)))


class ZeroOrMore(Rule):
    """
    Match a rule ad infinitum. This rule is similar to the Optional()
    rule. While this one only matches if the subrule matches 0 or 1
    times, the ZeroOrMore rule matches at any time. This rule tries to
    consume as much input as possible.
    """
    def __init__(self, rule):
        """
        Initialize this rule with a subrule. The subrule is
        transformed to a Optional(OneOrMore(rule)) construct.

        @param rule: The subrule to match.
        @type  rule: Rule
        """
        self.rule = Optional(OneOrMore(rule))

    def __str__(self):
        """
        Return a human readable representation of the rule.

        @return A description of this rule.
        """
        return "{ %s }" % str(self.rule)

    def match(self, input_reader):
        """
        Match the input against the subrule.

        @param input_reader: The input reader to read from.
        @type  input_reader: InputReader
        @return: A list of token generated by the matching of the subrule.
        """
        retval = self.rule.match(input_reader)
        return self.returnToken(self.callAction(retval))


class IgnoreWhite(Rule):
    """
    A pseudo-rule to tell the parser to temporary ignore
    whitespaces. This rule itself does not match anything. It merely
    sets the input reader into 'ignore whitespace' mode and returns
    the token produced by its subrule. After executing the subrule,
    the ignore state of the input reader is reset (i.e. if it was
    'ignore' before, it will be afterwards, if it was 'match', it will
    be that).
    """
    def __init__(self, rule):
        """
        Initialize the rule with a subrule.

        @param rule: The subrule to match.
        @type  rule: Rule
        """
        self.rule = rule

    def __str__(self):
        """
        Return a human-readable representation of this rule.

        @return: A string describing this rule.
        """
        return "IgnoreWhite(%s)" % str(self.rule)

    def match(self, input_reader):
        """
        Match the input against this rule. The input reader is set to
        'ignore whitespace' mode, the subrule is matched, the ignore
        state of the input reader is reset and the result of the
        subrule is returned.

        @param input_reader: The input reader to read any input from.
        @type  input_reader: InputReader
        @return: The results of the subrule.
        """
        ignore = input_reader.getIgnoreState()
        input_reader.setIgnoreState(True)
        try:
            result = self.rule.match(input_reader)
        except:
            input_reader.setIgnoreState(ignore)
            raise
        input_reader.setIgnoreState(ignore)
        return self.returnToken(self.callAction(result))


class MatchWhite(Rule):
    """
    A pseudo-rule to tell the parser to temporary match
    whitespaces. This rule is the counterpart of the IgnoreWhite
    rule. It sets the input reader into 'match whitespace' mode and
    matches the given subrule.
    """
    def __init__(self, rule):
        """
        Initialize this rule with a subrule.

        @param rule: The rule to match as a subrule.
        @type  rule: Rule
        """
        self.rule = rule

    def __str__(self):
        """
        Return a human-readable description of the rule.

        @return: A human-readable description of this rule.
        """
        return "MatchWhite(%s)" % str(self.rule)

    def match(self, input_reader):
        """
        Match this rule against the input. The rule sets the input
        reader into 'match whitespace' mode, matches the subrule,
        resets the ignore state and returns the results of the
        subrule.

        @param input_reader: The input reader to read input from.
        @type  input_reader: InputReader
        @return: A list of token generated by the subrule.
        """
        ignore = input_reader.getIgnoreState()
        input_reader.setIgnoreState(False)
        # skip the trailing whitespace before the subrule matches.
        input_reader.skipWhite()
        try:
            result = self.rule.match(input_reader)
        except:
            input_reader.setIgnoreState(ignore)
            raise
        input_reader.setIgnoreState(ignore)        
        return self.returnToken(self.callAction(result))


class Alpha(Rule):
    #Match a string containing only letters.     
    def __init__(self, string):        
        self.string = string

    def __str__(self):
        #Return a human-readable description of the rule.
        #@return: A human-readable description of this rule.        
        return "Alpha(%s)" % str(self.string)

    def match(self, input_reader):
        #Match the input 
        #@param input_reader: The input reader to read input from.
        #@type  input_reader: InputReader
        #@return: The matched character, if any.        
        input_reader.checkPoint()
        try:            
            string = input_reader.getString(len(self.string))
            # The input does not match our string 
            if not(string.isAlpha()):
                # Roll back the parse 
                input_reader.rollback()
                #raise ParseException()
                #raise ParseException("Expected '%s' at position %d. Got '%s'" % (self.string, input_reader.getPos(), string))
        except EndOfStringException: 
            # End of string reached without a match 
            input_reader.rollback()
            #raise ParseException()
            #raise ParseException("Expected '%s' at end of string" % self.string)
        # We have a successful match, so delete the checkpoint.  
        input_reader.deleteCheckpoint()
        logging.debug("Matched \"%s\"" % self)
        # Return the string and call its action (if it has one).  
        return self.returnToken(self.callAction([string]))
           
           
class Digit(Rule):
    #Match a string containing only digits.     
    def __init__(self, string):        
        self.string = str(string) 

    def __str__(self):
        #Return a human-readable description of the rule.
        #@return: A human-readable description of this rule.        
        return "Digit(%s)" % str(self.rule)

    def match(self, input_reader):
        #Match the input 
        #@param input_reader: The input reader to read input from.
        #@type  input_reader: InputReader
        #@return: The matched character, if any.        
        input_reader.checkPoint()
        try:
            string = input_reader.getString(len(self.string))
            # The input does not match our string 
            if not(string.isDigit()):
                # Roll back the parse 
                input_reader.rollback()
                #raise ParseException()
                #raise ParseException("Expected '%s' at position %d. Got '%s'" % (self.string, input_reader.getPos(), string))
        except EndOfStringException: 
            # End of string reached without a match 
            input_reader.rollback()
            #raise ParseException()
            #raise ParseException("Expected '%s' at end of string" % self.string)
        # We have a successful match, so delete the checkpoint.  
        input_reader.deleteCheckpoint()
        logging.debug("Matched \"%s\"" % self)
        # Return the string and call its action (if it has one).  
        return self.returnToken(self.callAction([string]))           


class Alnum(Rule):
    #Match a string containing letters and digits.      
    def __init__(self, string):        
        self.string = string

    def __str__(self):
        #Return a human-readable description of the rule.
        #@return: A human-readable description of this rule.        
        return "Alnum(%s)" % str(self.string)

    def match(self, input_reader):
        #Match the input 
        #@param input_reader: The input reader to read input from.
        #@type  input_reader: InputReader
        #@return: The matched character, if any.        
        input_reader.checkPoint()
        try:
            string = input_reader.getString(len(self.string))
            # The input does not match our string 
            if not(string.isAlnum()):
                # Roll back the parse 
                input_reader.rollback()
                #raise ParseException()
                #raise ParseException("Expected '%s' at position %d. Got '%s'" % (self.string, input_reader.getPos(), string))
        except EndOfStringException: 
            # End of string reached without a match 
            input_reader.rollback()
            #raise ParseException()
            #raise ParseException("Expected '%s' at end of string" % self.string)
        # We have a successful match, so delete the checkpoint.  
        input_reader.deleteCheckpoint()
        logging.debug("Matched \"%s\"" % self)
        # Return the string and call its action (if it has one).  
        return self.returnToken(self.callAction([string]))

           
#  Useful parsers  
integer  = Word(Digit) 
letters  = Word(Alpha)  

hexdigit = AnyOf('0123456789abcdefABCDEF')
     
                                      
def parse(parser, string, ignore_white=True): 
    input_reader = InputReader(string, ignore_white)
    tokens = parser.match(input_reader)
    return ParseResult(input_reader, tokens)


#  A function to parse input
def parseit(grammar_name, input):
    result = parse(grammar_name, input)

    if result.full(): 
       print "Success!" 
    else: 
       print "Fail"  




