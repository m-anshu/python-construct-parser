import ply.lex as lex

# var = lambda a,b : (a+b)*6

def temp(a,b):
    return a+b
var = temp

tokens = (
    'LAMBDA',
    'COLON',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'IDENTIFIER',
    'EQUALS',
    'COMMA'
)

t_COLON   = r':'
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_EQUALS  = r'\='
t_ignore  = ' \t'
t_COMMA   = r'\,'

def t_LAMBDA(t):
    r'lambda'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_lambda_func(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

# data = '''lambda a, b, c, rfge, audhe, adhf8e7f9 : a + b'''

# lexer.input(data)

# # Tokenize
# while True:
#     tok = lexer.token()
#     if not tok: 
#         break      # No more input
#     print(tok)