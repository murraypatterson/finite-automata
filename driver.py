from FAParser import parser
from FA import DFA
from itertools import product

# generate all strings on an alphabet upto length m-1
def atm(sig, m) :

    result = []
    for i in range(m) :
        for string in product(sig, repeat = i) :
            result.append(''.join(string))

    return result

# Main
#----------------------------------------------------------------------

# parse info from FA encoding and display it

data = open('even.dfa').read()
start, finals, transitions = parser.parse(data)

print('start:', start)
print('finals:', finals)
print('transitions:', transitions)

# build DFA with this info

sig = set(t[1] for t in transitions) # obtain alphabet
print('alphabet:', sig)

dfa = DFA(sig,set()) # build DFA from alphabet, etc...

# ...

# generate all strings on the alphabet upto length 4 and print them

at5 = atm(sig, 5)
print(at5)

# ...
