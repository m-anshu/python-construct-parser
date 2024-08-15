import ply.lex as lex
import ply.yacc as yacc

# def identifier(arguments_list): expr

tokens = (
    'DEF',
    'COLON',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'IDENTIFIER',
    'COMMA'
)

t_COLON   = r':'
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_ignore  = ' \t'
t_COMMA   = r'\,'

def t_DEF(t):
    r'def'
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

# def identifier(arguments_list): expr

def p_function_declaration(p):
    '''function_declaration : DEF IDENTIFIER LPAREN argument_list RPAREN COLON
                            | DEF IDENTIFIER LPAREN RPAREN COLON'''

    print("valid syntax")

def p_argument_list_single(p):
    '''argument_list : IDENTIFIER
                     | expression'''
    p[0] = [p[1]]

def p_argument_list_multiple(p):
    '''argument_list : argument_list COMMA IDENTIFIER
                     | argument_list COMMA expression'''
    p[0] = p[1] + [p[3]]

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

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