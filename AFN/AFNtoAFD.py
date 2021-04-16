import json

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
        print(elem)
        for item in elem:
            if str(item) == 'q0':
                aux.append(elem)

with open('AFN/AFNjson.json','r') as json_file:
    AFNjson = json.load(json_file)

E = AFNjson['E'] #Correto
Q = list(powerset(AFNjson['Q']))[1:] #Será o powerset
Q0 = AFNjson['Q0'] #Correto
F = to_tuple(AFNjson['F']) #As transições usam a lista de estado como estado
QF = AFNjson['QF']  # Powerset de QF tais que a interseção não seja nula entre os automatos

def convert_to_AFD(E,Q,F,Q0,QF,C):
    Q = states_to_string(list(powerset(Q))[1:])
    Q0 = str([Q0])
    F = to_state(to_tuple(F))

print(Q)
# print(type(QF[0]))
print(fn_to_fd(Q,QF))
