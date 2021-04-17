import sys
import json


#  INICIO DO AUTOMATO  #
#      FINITO NÃO      #
#    DETERMINISTICO    #


def pertence(E, t):  # Verifica se o teste pertence aos simbolos de entrada
    if t in E:
        return 0
    else:
        return 1

class data: #Objeto que guarda a execução do automato
    steps = []
    fsteps = []
    state = ""


def afnd_start(E, Q, F, Q0, QF, C):  # Função do automato inteiro
    jsonR = data()
    jsonR.steps = []
    jsonR.fsteps = []

    def afnd_rec(E, Q, F, Q0, QF, C):  # Função para a recursão

        # Verifica de começo se a cadeia é vazia, já resolvendo caso comecar o automato com uma cadeia vazia
        if len(C) == 0:
            if Q0 in QF:
                return 0
            else:
                return 1

        func = False

        if pertence(E, C[0]) == 1:   # Verifica se existe no alfabeto
            print("Erro, simbolo não existe no alfabeto!")
            jsonR.fsteps.append([Q0,C[0],"[]"])
            return 1

        for index in range(0, len(F)):   # Busca função de transição
            if F[index][0] == Q0:        # Encontra estado atual nas funções
                if F[index][1] == C[0]:  # Encontra elemento da cadeia na função
                    func = True
                    jsonR.fsteps.append([Q0,C[0],F[index][2]])
                    for est in range(0, len(F[index][2])):
                        if afnd_rec(E, Q, F, F[index][2][est], QF, C[1:]) == 0:  # recursão
                            jsonR.steps.append([Q0,C[0],F[index][2]])
                            return 0

        if func == False:
            return 1

    result = afnd_rec(E, Q, F, Q0, QF, C)

    if result == 0:  # Printa se foi sucesso ou fracasso
        print("Sucesso")
        jsonR.steps.reverse()
        jsonR.state = "APROVADO!"
    else:
        print("Fracasso")
        jsonR.state = "RECUSADO!"

    jsondata = {
        "steps": jsonR.steps,
        "fsteps": jsonR.fsteps,
        "state": jsonR.state
    }
    
    with open("AFN/AFNresults.json","w") as write_file:
        json.dump(jsondata,write_file)

    return


# MAIN
#afnd_start(E, Q, F, Q0, QF, C)