import ply.yacc as yacc
from FALexer import tokens

def p_dfa(p):
  'dfa : start final transitions'
  p[0] = (p[1],p[2],p[3])

def p_start(p):
  'start : START NAME'
  p[0] = p[2]

def p_final(p):
  'final : FINAL names'
  p[0] = p[2]

def p_names_1(p):
  'names : '
  p[0] = []

def p_names_2(p):
  'names : names NAME'
  p[0] = p[1] + [p[2]]

def p_transitions_1(p):
  'transitions : transition'
  p[0] = [p[1]]

def p_transitions_2(p):
  'transitions : transitions transition'
  p[0] = p[1] + [p[2]]

def p_transition_1(p):
  'transition : TRANS NAME COLON NAME COLON NAME'
  p[0] = (p[2],p[4],p[6])

def p_transition_2(p):
  'transition : TRANS NAME COLON COLON NAME'
  p[0] = (p[2],"",p[5])

def p_error(p):
  print("Syntax error in input!")

parser = yacc.yacc()
