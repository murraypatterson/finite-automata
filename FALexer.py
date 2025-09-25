import ply.lex as lex

reserved = { 'start': 'START', 'final': 'FINAL', 'trans': 'TRANS' }

tokens = ['NAME','COLON'] + list(reserved.values())

t_COLON = r':'
t_START = r'[sS][tT][aA][rR][tT]'
t_FINAL = r'[fF][iI][nN][aA][lL]'
t_TRANS = r'[tT][rR][aA][nN][sS]'

def t_NAME(t):
  r'[_a-zA-Z0-9]+'
  t.type = reserved.get(t.value.lower(),'NAME')
  return t

# Ignored characters
t_ignore = " \r\n\t"
t_ignore_COMMENT = r'\#.*'

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  #t.lexer.skip(1)
  raise Exception('LEXER ERROR')

lexer = lex.lex()
## Test it out
#data = '''
#start q0
#final q1 q3
#q0:a:q1
#q0:a:q2
#q2:b:q3
#q3:a:q2
#'''

#data = open('even.dfa','r').read() # or try from a file

## Give the lexer some input
#print("Tokenizing:", data)
#lexer.input(data)

## Tokenize
#while True:
#  tok = lexer.token()
#  if not tok: 
#    break      # No more input
#  print(tok)
