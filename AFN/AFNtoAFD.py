import json
import sys
import AFNtoAFDGUI


def powerset(s):
    x = len(s)
    masks = [1 << i for i in range(x)]
    for i in range(1 << x):
        yield [ss for mask, ss in zip(masks, s) if i & mask]

def to_tuple(f):
    aux = [tuple(elem) for elem in f]
    return aux

def to_state(f):
    aux = []
    for elem in f:
        aux.append((elem[0],elem[1],str(elem[2])))
    return aux

def states_to_string(q):
    aux = []
    for elem in q:
        aux.append(str(elem))
    return aux

def fn_to_fd(q,qf):
    aux = []
    for elem in q:
        for item in elem:
            if item in qf:
                aux.append(elem)
    return aux

def convert_to_AFD(E,Q,F,Q0,QF):
    QF = fn_to_fd(Q,QF)
    Q = states_to_string(list(powerset(Q))[1:])
    Q0 = str([Q0])
    F = to_state(to_tuple(F))
    AFNtoAFDGUI.StartAFDtoAFNGUI(E,Q,F,Q0,QF)



