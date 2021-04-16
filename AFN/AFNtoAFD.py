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
        aux.append([str(elem[0]),elem[1],str(elem[2])])
    return aux

def fetch_funcs(f,q,e):
    for elem in f:
        if q == elem[0] and e == elem[1]:
            return elem[2]
    return []

def qn_to_fd(f,q,e):
    funcs = []
    for s in e:
        simbol_list = []
        for elem in list(powerset(q))[1:]:
            elem_list = []
            for i in elem:
                aux = fetch_funcs(f,i,s)
                for j in aux:
                        elem_list.append(j)
            if elem_list != []:
                funcs.append([elem,s,elem_list])

    return funcs

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

with open('AFN/AFNjson.json','r') as json_file:
    AFNjson = json.load(json_file)

E = AFNjson['E'] #Correto
Q = AFNjson['Q'] #Será o powerset
Q0 = AFNjson['Q0'] #Correto
F = AFNjson['F'] #As transições usam a lista de estado como estado
QF = AFNjson['QF']  # Powerset de QF tais que a interseção não seja nula entre os automatos

def convert_to_AFD(E,Q,F,Q0,QF):
    F = to_state(qn_to_fd(F,Q,E))
    QF = states_to_string(fn_to_fd(list(powerset(Q)),QF))
    Q = states_to_string(list(powerset(Q)))
    Q0 = str([Q0])

    jsondata = {
        'E': E,
        'Q': Q,
        'Q0': Q0,
        'F': F,
        'QF': QF
    }

    with open('AFN/AFNConverted.json','w') as write_file:
        json.dump(jsondata,write_file)

convert_to_AFD(E,Q,F,Q0,QF)