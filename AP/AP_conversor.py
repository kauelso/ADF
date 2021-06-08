import json

#Pilha vazia
E = "01"
Q = ["q0", "q1", "q2"]
EP = ["0","1","Z0"]
F = [["q0", "0", "Z0", ["q0", ["0","Z0"]]], ["q0", "1", "Z0", ["q0", ["1","Z0"]]], ["q0", "0", "0", ["q0", "00"]], ["q0", "0", "1", ["q0", "01"]], ["q0", "1", "0", ["q0", "10"]], ["q0", "1", "1", [
    "q0", "11"]], ["q0", "", "Z0", ["q1", ["Z0"]]], ["q0", "", "0", ["q1", "0"]], ["q0", "", "1", ["q1", "1"]], ["q1", "0", "0", ["q1", ""]], ["q1", "1", "1", ["q1", ""]], ["q1", "", "Z0", ["q2", ""]]]
Q0 = "q0"
Z0 = "Z0"
QF = ["q2"]   # pra aceitaçao por pilha vazia, qf é inutil
C = '1001'

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

def addNewStates(q,q0,f,z0,x0):
    novoq0 = createState(q) #cria novo estado inicial
    q.append(novoq0)
    qf = createState(q) #cria novo estado final
    q.append(qf)
    f.append([novoq0, "", x0, [q0, [z0,x0]]]) #estado incial novo transiciona para estado incial antigo
    buildFinalTransitions(f,qf,x0,z0)
    return [novoq0,qf]

def convertPvParaEf(E,Q,EP,F,Q0,Z0):
    x0 = setZ0(Z0,EP)
    nq = addNewStates(Q,Q0,F,Z0,x0)
    EP.append(x0)
    
    jsonData = {
        "E": E,
        "Q": Q,
        "EP": EP,
        "F": F,
        "Q0": nq[0],
        "Z0": x0,
        "QF": nq[1]
    }

    with open("AP/PVparaEF.json",'w') as write_file:
        json.dump(jsonData,write_file)

convertPvParaEf(E,Q,EP,F,Q0,Z0)
