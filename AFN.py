import sys


# Parte dos dados
E = '01'  # Simbolos de entrada
Q = ['q0', 'q1', 'q2']  # Lista de estados
# Função de transição (Lista de tuplas) - [(Estado atual, simbolo, [proximos estados]),...]
F = [("q0", "0", ["q0"]), ("q0", "1", ["q0", "q1"]), ("q1", "0", ["q2"]),
     ("q2", "1", ["q3"]), ("q3", "0", ["q3"]), ("q3", "1", ["q3"])]
Q0 = 'q0'  # Estado inicial
QF = ['q3']  # Lista de estados finais
C = "11"  # Cadeia de teste


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
                return 1

        func = False

        if pertence(E, C[0]) == 1:   # Verifica se existe no alfabeto
            print("Erro, simbolo não existe no alfabeto!")
            sys.exit()

        for index in range(0, len(F)):   # Busca função de transição
            if F[index][0] == Q0:        # Encontra estado atual nas funções
                if F[index][1] == C[0]:  # Encontra elemento da cadeia na função
                    func = True
                    for est in range(0, len(F[index][2])):
                        if afnd_rec(E, Q, F, F[index][2][est], QF, C[1:]) == 0:  # recursão
                            return 0

        if func == False:
            return 1

    result = afnd_rec(E, Q, F, Q0, QF, C)

    if result == 0:  # Printa se foi sucesso ou fracasso
        print("Sucesso")
    else:
        print("Fracasso")
    return


# MAIN
afnd_start(E, Q, F, Q0, QF, C)
