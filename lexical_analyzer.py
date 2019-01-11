charClass = 0
lexeme = 'a'
nextChar = 'a'
lexLen = 0
token = 0
nextToken = 0
charPos = 0

EOF = None
LETTER = 0
DIGIT = 1
UNKNOWN = 99

# TOKEN CODES
INT_LIT = 10
IDENT = 11
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
MULT_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26

FOR_CODE = 30
IF_CODE = 31
ELSE_CODE = 32
WHILE_CODE = 33
DO_CODE = 34
INT_CODE = 35
FLOAT_CODE = 36
SWITCH_CODE = 37

in_fp = open("front.in","r")
txtdata = in_fp.read()
N = len(txtdata)

def main() :
    if (in_fp == None) :
        print("ERROR - cannot open front.in \n")
    else :
        getChar()
        while nextToken != EOF :
            lex()
    in_fp.close()
    return 0
     
# lookUp
def lookup(ch) :
    global nextToken
    if ch == '(':
        addChar()
        nextToken = LEFT_PAREN
    elif ch == ')':
        addChar()
        nextToken = RIGHT_PAREN
    elif ch == '+':
        addChar()
        nextToken = ADD_OP
    elif ch == '-':
        addChar()
        nextToken = SUB_OP
    elif ch == '*':
        addChar()
        nextToken = MULT_OP
    elif ch == '/':
        addChar()
        nextToken = DIV_OP
    else :
        addChar()
        nextToken = EOF
    return nextToken
   
#AddChar
def addChar() :
    global lexeme
    if lexLen <= 98 :
        if lexeme == ' ' :
            lexeme = nextChar
        else :
            lexeme = lexeme + nextChar
    else :
        print("Error - lexeme is too long \n")


#getChar
def getChar() :
    global charPos
    global nextChar
    global charClass
    
    if N > charPos :
        nextChar = txtdata[charPos]
        charPos = charPos + 1
    else :
        nextChar = EOF
        charPos = charPos + 1
        
    if nextChar != EOF :
        if nextChar.isalpha() :
            charClass = LETTER
        elif nextChar.isdigit() :
            charClass = DIGIT
        else :
            charClass = UNKNOWN
    else :
        charClass = EOF

# getNonBlank
def getNonBlank() :
    if nextChar != EOF :
        while nextChar.isspace() :
            getChar()

#lex
def lex() :
    global lexeme
    global charClass
    global nextToken
    lexeme = ' '
    lexLen = 0
    getNonBlank()
    if charClass == LETTER :
        addChar()
        getChar()
        while ((charClass == LETTER) or (charClass == DIGIT)) :
            addChar()
            getChar()

        if lexeme == 'for' :
            nextToken = FOR_CODE
        elif lexeme == 'if' :
            nextToken = IF_CODE
        elif lexeme == 'else' :
            nextToken = ELSE_CODE
        elif lexeme == 'while' : 
            nextToken = WHILE_CODE
        elif lexeme == 'do' : 
            nextToken = DO_CODE
        elif lexeme == 'int' : 
            nextToken = INT_CODE
        elif lexeme == 'float' : 
            nextToken = FLOAT_CODE
        elif lexeme == 'switch' :
            nextToken = SWITCH_CODE
        else :
            nextToken = IDENT
    
    # parse ints lits
    elif charClass == DIGIT :
        addChar()
        getChar()
        while (charClass == DIGIT) :
            addChar()
            getChar()
        
        nextToken = INT_LIT

    #pares and ops
    elif charClass == UNKNOWN :
       lookup(nextChar)
       getChar()

    #EOF
    elif charClass == EOF :
        nextToken = EOF
        lexeme = 'EOF'
    # end of switch
    print("Next token is:",nextToken," next lexeme is",lexeme)
    return nextToken
# end of lex()

main()
