import ply.lex as lex
import ply.yacc as yacc

# Lexer
tokens = (
    'IMPORT',
    'AS',
    'FROM',
    'STAR',
    'COMMA',
    'ID',
)

t_STAR = r'\*'
t_COMMA = r','
t_ignore = ' \t'

def t_AS(t):
    r'as'
    return t
def t_FROM(t):
    r'from'
    return t
def t_IMPORT(t):
    r'import'
    return t
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer=lex.lex();

# Parser
def p_import_statement(p):
    '''
    import_statement : IMPORT ID
                    | IMPORT ID AS ID
                    | FROM ID IMPORT ID
                    | FROM ID IMPORT ID AS ID
                    | FROM ID IMPORT STAR
                    | FROM ID IMPORT ID COMMA ID
    '''
    print("Valid Syntax")

def p_error(p):
    if p:
        error_token = p.value
        position = p.lexpos
        line_number = p.lineno
        print(f"Syntax error at line {line_number}, character position {position}: Unexpected token '{error_token}'")
    else:
        print("Syntax error at EOF")


parser = yacc.yacc()

# Test the parser
input_text=input()

lexer.input(input_text)
for tok in lexer:
    print(tok)

result = parser.parse(input_text)

