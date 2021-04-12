import sys
import json


# Parte dos dados
E = '01'  # Simbolos de entrada
Q = ['q0', 'q1', 'q2']  # Lista de estados
# Função de transição (Lista de tuplas) - [(Estado atual, simbolo, proximo estado),...]  Funçao ε deve ser tratada como " " ex: ("q2", " ", "q3")
F = [("q1", "0", "q1"), ("q1", "1", "q1"),
     ("q1", "1", "q2"), ("q2", "0", "q3"), ("q2", "", "q3"), ("q3", "", "q4"), ("q4", "0", "q4"), ("q4", "1", "q4")]
Q0 = 'q1'  # Estado inicial
QF = ['q4']  # Lista de estados finais
C = "1"  # Cadeia de teste

class data: #Objeto que guarda a execução do automato
    steps = []
    state = ""


#  INICIO DO AUTOMATO  #
#      FINITO NÃO      #
#    DETERMINISTICO    #


def pertence(E, t):  # Verifica se o teste pertence aos simbolos de entrada
    if t in E:
        return 0
    else:
        return 1


def afnd_start(E, Q, F, Q0, QF, C):  # Função do automato inteiro

    def afnd_rec(E, Q, F, Q0, QF, C):  # Função para a recursão

        # Verifica de começo se a cadeia é vazia, já resolvendo caso comecar o automato com uma cadeia vazia
        if len(C) == 0:
            if Q0 in QF:
                return 0
            else:
                # Tratamento quando a C termina e ainda existe cadeia vazia possiveis na função
                for var in range(0, len(F)):
                    if F[var][0] == Q0 and F[var][1] == '':
                        if afnd_rec(E, Q, F, F[var][2], QF, C) == 0:
                            return 0
                return 1

        func = False

        if pertence(E, C[0]) == 1:   # Verifica se existe no alfabeto
            print("Erro, simbolo não existe no alfabeto!")
            sys.exit()

        for index in range(0, len(F)):   # Busca função de transição
            if F[index][0] == Q0:        # Encontra estado atual nas funções
                if F[index][1] == C[0]:  # Encontra elemento da cadeia na função
                    func = True
                    if afnd_rec(E, Q, F, F[index][2], QF, C[1:]) == 0:  # recursão
                        return 0
                if F[index][1] == '':   # Encontra cadeia vazia na função
                    func = True
                    if afnd_rec(E, Q, F, F[index][2], QF, C) == 0:  # recursão
                        return 0

        if func == False:
            return 1

    result = afnd_rec(E, Q, F, Q0, QF, C)

    if result == 0:  # Printa se foi sucesso ou fracasso
        print("Sucesso")
        results.state = "APROVADO!"
        

    else:
        print("Fracasso")
        results.state = "REJEITADO!"
    return


# MAIN
afnd_start(E, Q, F, Q0, QF, C)
