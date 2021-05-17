import sys
import ER_conver_AFNE as ER_AFNE
import infix_to_prefix as intp
import json

#  INICIO DO AUTOMATO  #
#      FINITO NÃO      #
#    DETERMINISTICO    #
#     COM CADEIAS      #
#        VAZIAS        #

def pertence(E, t):  # Verifica se o teste pertence aos simbolos de entrada
    if t in E:
        return 0
    else:
        return 1


def afne_start(E, Q, F, Q0, QF, C):  # Função do automato inteiro
    trace = []

    def afne_rec(E, Q, F, Q0, QF, C):  # Função para a recursão

        # Verifica de começo se a cadeia é vazia, já resolvendo caso comecar o automato com uma cadeia vazia
        if len(C) == 0:
            if Q0 in QF:
                return 0
            else:
                # Tratamento quando a C termina e ainda existe cadeia vazia possiveis na função
                for var in range(0, len(F)):
                    if F[var][0] == Q0 and F[var][1] == '':
                        for est in range(0, len(F[var][2])):
                            if afne_rec(E, Q, F, F[var][2][est], QF, C) == 0:  # recursão
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
                    for est in range(0, len(F[index][2])):
                        if afne_rec(E, Q, F, F[index][2][est], QF, C[1:]) == 0:  # recursão
                            return 0
                if F[index][1] == '':   # Encontra cadeia vazia na função
                    func = True
                    for est in range(0, len(F[index][2])):
                        if afne_rec(E, Q, F, F[index][2][est], QF, C) == 0:  # recursão
                            return 0

        if func == False:
            return 1

    result = afne_rec(E, Q, F, Q0, QF, C)

    if result == 0:  # Printa se foi sucesso ou fracasso
        print("Sucesso")
    else:
        print("Fracasso")
    return