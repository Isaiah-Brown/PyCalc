# -----------------------------------------------------------------------------
# calclex.py
# -----------------------------------------------------------------------------
import ply.lex as lex

tokens = (
    'NUMBER',
    'PLUS','MINUS','TIMES','DIVIDE', 'POWER', 'FACTORIAL', 'SIN', 'COS', 'EQUALS',
    'LPAREN','RPAREN',
    )

# Tokens

t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_POWER     = r'\^'
t_FACTORIAL = r'\!'
t_SIN       = r'sin'
t_COS       = r'cos'
t_EQUALS    = r'='
t_LPAREN    = r'\('
t_RPAREN    = r'\)'

def t_NUMBER(t):
    r'(\d+)?[\.bx]?[0-9A-F]+'
    t_string = str(t.value)

    if '0b' == t_string[0:2]:
        binary_number = t_string[2:][::-1]
        num = 0

        for i in range(len(binary_number)):
            try:
                value = int(binary_number[i])
            except ValueError:
                print("Binary representation error %s" % t.value)
                t.value = 0
                return t
            if value == 1:
                base = pow(2, i) 
                num += base

        t.value = num
        return t
   
    elif '0x' == t_string[0:2]:
        hex_number = t_string[2:][::-1]
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F']
        num = 0
        for i in range(len(hex_number)):
            value = hex_number[i]
            base = pow(16, i)
            if value in alphabet:
                num += base * (10 + alphabet.index(value))
            else:
                num += base * (int(value))
        t.value = num
        return t

    elif '.' in t_string:
        try: 
            t.value = float(t.value)
        except ValueError:
            print("Float representation error %s" % t.value)

    else:
        try:
            t.value = int(t.value)
        except ValueError:
            print("Cannot parse the number: %s" % t.value)
            t.value = 0

    return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build the lexer
lexer = lex.lex()



# Test it output
def test(data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok: 
            break
        print(tok)

if __name__ == "__main__":
    test_str = input("lex_test > ")
    while test_str != "":
        test(test_str)
        test_str = input("lex_test > ")
    
