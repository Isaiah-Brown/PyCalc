import math
# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from calclex import tokens

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

def p_term_pow(p):
    'term : term POWER factor'
    p[0] = pow(p[1], p[3])

def p_term_factorial(p):
    'term : term FACTORIAL'
    num = int(p[1])
    output = 1
    while num != 0:
        output *= num
        num -= 1
    p[0] = output
    
def p_term_sin(p):
    'factor : SIN term'
    p[0] = math.sin(float(p[2]))

def p_term_cos(p):
    'factor : COS term'
    p[0] = math.cos(float(p[2]))

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = input('calc> ')
   except EOFError:
       break
   if not s:
       continue
   result = parser.parse(s)
   print(result)
