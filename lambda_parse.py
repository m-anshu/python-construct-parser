import ply.lex as lex

# var = lambda a,b : (a+b)*6

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

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

import ply.yacc as yacc

# var = lambda a,b : (a+b)*6
# a, b, c, d, e, f
# ["a", "b", c, d, e, f]
# "a" + 1 that throws error

def p_lambda_funtion(p):
    'lambda_function : IDENTIFIER EQUALS LAMBDA argument_list COLON expression'
    print("valid syntax")
    #       0               1        2     3           4        5       6
    def temp(): 
        return p[6]
    p[1] = temp

def p_argument_list_single(p):
    'argument_list : IDENTIFIER'
    p[0] = [p[1]]

def p_argument_list_multiple(p):
    'argument_list : argument_list COMMA IDENTIFIER'
    p[0] = p[1] + [p[3]]

def p_factor_identifier(p):
    '''expression : IDENTIFIER 
                  | expression'''
    p[0] = sum([ord(x) for x in p[1]])

def p_expression_plus(p):
    'expression : expression PLUS term'
    

def p_expression_minus(p):
    'expression : expression MINUS term'
    

def p_expression_term(p):
    'expression : term'
    

def p_term_times(p):
    'term : term TIMES factor'
    

def p_term_div(p):
    'term : term DIVIDE factor'
    

def p_term_factor(p):
    '''term : factor
            | IDENTIFIER'''
    

def p_factor_num(p):
    'factor : NUMBER'
    

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    

def p_error(p):
    if p:
        error_token = p.value
        position = p.lexpos
        line_number = p.lineno
        print(f"Syntax error at line {line_number}, character position {position}: Unexpected token '{error_token}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

input_r_code = input()
result = parser.parse(input_r_code, lexer=lexer)
lexer.input(input_r_code)
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(f"LexToken({tok.type}, {tok.value}, {tok.lineno}, {tok.lexpos})")
