
class DFA:

  def __init__(self,sig,q=set()):
    self.sigma = sig
    self.states = q
    self.delta = {}
    self.start = None
    self.final = None

  # getters and setters

  # add state s to DFA
  def add_state(self,s):
    pass

  # add transition (f,c,t) to DFA
  def add_transition(self,f,c,t):
    pass

  # to String method
  def __str__(self):
    pass

  # ...
