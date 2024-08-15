import ply.lex as lex
import ply.yacc as yacc

# Define the tokens
tokens = (
    'ID',
    'LBRACKET',
    'RBRACKET',
    'EQUALS',
    'FOR',
    'IN',
    'NUMBER',
    'STRING',   
    'IF',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)

# Define the token rules
t_TIMES = r'\*'
t_EQUALS = r'='
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_ignore = ' \t'
t_PLUS = r'\+'
t_MINUS = r'-'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_IF(t):
    r'if'
    return t
def t_IN(t):
    r'in'
    return t
def t_FOR(t):
    r'for'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = 'ID'
    return t

def t_STRING(t):
    r'("[^"]*")|(\'[^\']*\')'
    t.type='STRING'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Define the grammar rules
def p_list_comprehension(p):
    '''
    list_comprehension : ID EQUALS LBRACKET expression FOR ID IN ID IF ID IN ID RBRACKET
                      | ID EQUALS LBRACKET expression FOR ID IN ID RBRACKET
                      | ID EQUALS LBRACKET expression FOR ID IN ID IF STRING IN ID RBRACKET
    '''
    print("Valid list comprehension")

def p_expression(p):
    '''
    expression : expression PLUS term
               | expression MINUS term
               | term
    '''

def p_term(p):
    '''
    term : term TIMES factor
         | term DIVIDE factor
         | factor
    '''

def p_factor(p):
    '''
    factor : LPAREN expression RPAREN
           | NUMBER
           | ID
    '''



def p_error(p):
    if p:
        error_token = p.value
        position = p.lexpos
        line_number = p.lineno
        print(f"Syntax error at line {line_number}, character position {position}: Unexpected token '{error_token}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

input_string = input()
lexer.input(input_string)
parser.parse(lexer=lexer)
