from FAParser import parser
from FA import NFA
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

data = open('asborabs.nfa').read()
start, finals, transitions = parser.parse(data)

print('start:', start)
print('finals:', finals)
print('transitions:', transitions)

# build NFA with this info

sig = set(t[1] for t in transitions) # obtain alphabet
print('alphabet:', sig)

nfa = NFA(sig, set()) # build NFA from alphabet, etc...

# ...

# generate all strings on the alphabet upto length 4 and print them

at5 = atm(sig, 5)
print(at5)

# ...
