import json

def setZ0(z,e):
    count = 0
    while True:
        countS = str(count)
        if ("X"+countS) not in z or ("X"+countS) not in e:
            return "X"+countS
        else:
            count = count + 1

def createState(q):
    count = 0
    while True:
        countS = str(count)
        if ("q"+countS) not in q:
            return "q"+countS
        else:
            count = count + 1

def buildFinalTransitions(f,qf,x0,z0):
    for elem in f:
        if elem[1] == "" and elem[2] == z0 and elem[3][1] == "":
            f.append([elem[3][0], "", x0, [qf, ""]])

def addNewStatesEF(q,q0,f,z0,x0):
    novoq0 = createState(q) #cria novo estado inicial
    q.append(novoq0)
    qf = createState(q) #cria novo estado final
    q.append(qf)
    f.append([novoq0, "", x0, [q0, [z0,x0]]]) #estado incial novo transiciona para estado incial antigo
    buildFinalTransitions(f,qf,x0,z0)
    return [novoq0,qf]

def addNewStatesPV(q,q0,f,z0,x0,qf,ep):
    novoq0 = createState(q) #cria novo estado inicial
    q.append(novoq0)
    novoqf = createState(q) #cria novo estado final
    q.append(novoqf)
    f.append([novoq0, "", x0, [q0, [z0,x0]]]) #estado incial novo transiciona para estado incial antigo
    
    for elem in qf:
        for simbol in ep:
            f.append([elem, "", simbol, [novoqf, ""]])
    for simbol in ep:
            f.append([novoqf, "", simbol, [novoqf, ""]])
    return novoq0

def convertEfParaPv(E,Q,EP,F,Q0,Z0,QF):
    x0 = setZ0(Z0,EP)
    EP.append(x0)
    nq = addNewStatesPV(Q,Q0,F,Z0,x0,QF,EP)
    jsonData = {
        "E": E,
        "Q": Q,
        "EP": EP,
        "F": F,
        "Q0": nq,
        "Z0": x0,
    }
    with open("AP/converted/EFparaPV.json",'w') as write_file:
        json.dump(jsonData,write_file)

def convertPvParaEf(E,Q,EP,F,Q0,Z0):
    x0 = setZ0(Z0,EP)
    nq = addNewStatesEF(Q,Q0,F,Z0,x0)
    EP.append(x0)
    
    jsonData = {
        "E": E,
        "Q": Q,
        "EP": EP,
        "F": F,
        "Q0": nq[0],
        "Z0": x0,
        "QF": [nq[1]]
    }

    with open("AP/converted/PVparaEF.json",'w') as write_file:
        json.dump(jsonData,write_file)

print("1--> Converte de PV para EF")
print("2--> Converte de EF para PV")

opt = input()

if opt == "1":
    with open('AP/data/AP_PV.json','r') as json_file:
        APjson = json.load(json_file)
    E = APjson["E"]
    Q = APjson["Q"]
    EP = APjson["EP"]
    F = APjson["F"]
    Q0 = APjson["Q0"]
    Z0 = APjson["Z0"]
    convertPvParaEf(E,Q,EP,F,Q0,Z0)
if opt == "2":
    with open('AP/data/AP_EF.json','r') as json_file:
        APjson = json.load(json_file)
    E = APjson["E"]
    Q = APjson["Q"]
    EP = APjson["EP"]
    F = APjson["F"]
    Q0 = APjson["Q0"]
    Z0 = APjson["Z0"]
    QF = APjson["QF"]
    print(QF)
    convertEfParaPv(E,Q,EP,F,Q0,Z0,QF)
