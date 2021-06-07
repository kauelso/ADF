import sys

E = "01"
Q = ["q0", "q1", "q2"],
EP = "01Z"
F = [["q0", "0", "Z", ["q0", "0Z"]], ["q0", "1", "Z", ["q0", "1Z"]], ["q0", "0", "0", ["q0", "00"]], ["q0", "0", "1", ["q0", "01"]], ["q0", "1", "0", ["q0", "10"]], ["q0", "1", "1", [
    "q0", "11"]], ["q0", "", "Z", ["q1", "Z"]], ["q0", "", "0", ["q1", "0"]], ["q0", "", "1", ["q1", "1"]], ["q1", "0", "0", ["q1", ""]], ["q1", "1", "1", ["q1", ""]], ["q1", "", "Z", ["q2", "Z"]]]
Q0 = "q0"
Z0 = "Z"
QF = ["q2"]
C = '0000'

#  INICIO DO AUTOMATO  #
#       DE PILHA       #
#      COM ESTADO      #
#        FINAL         #


def pertence(E, t):  # Verifica se o teste pertence aos simbolos de entrada
    if t in E:
        return 0
    else:
        return 1


def tratar(pilha, elem):    # Coloca e retira os elementos na pilha
    pilha2 = []
    for m in range(0, len(pilha)):
        pilha2.append(pilha[m])
    pilha2.pop()
    if elem == '':
        return pilha2
    else:
        elem = elem[::-1]
        for n in range(0, len(elem)):
            pilha2.append(elem[n])
        return pilha2


def apef_start(E, Q, EP, F, Q0, Z0, QF, C):
    pilha = [Z0]

    def apef_rec(E, Q, EP, F, Q0, Z0, QF, pilha, C):
        print(pilha, Q0)
        if len(C) == 0:
            if Q0 in QF:
                return 0
            else:
                ptopo = pilha[-1]
                for j in range(0, len(F)):
                    if F[j][0] == Q0 and F[j][1] == "" and F[j][2] == ptopo:
                        npilha = tratar(pilha, F[j][3][1])
                        if apef_rec(E, Q, EP, F, F[j][3][0], Z0, QF, npilha, C) == 0:
                            return 0

                return 1

        if pertence(E, C[0]) == 1:
            print("Erro, simbolo não existe no alfabeto!")
            sys.exit()

        if len(pilha) == 0:
            return 1

        for i in range(0, len(F)):
            ptop = pilha[-1]
            if F[i][0] == Q0 and F[i][1] == C[0] and F[i][2] == ptop:
                npilha = tratar(pilha, F[i][3][1])
                if apef_rec(E, Q, EP, F, F[i][3][0], Z0, QF, npilha, C[1:]) == 0:
                    return 0

            if F[i][0] == Q0 and F[i][1] == "" and F[i][2] == ptop:
                npilha = tratar(pilha, F[i][3][1])
                if apef_rec(E, Q, EP, F, F[i][3][0], Z0, QF, npilha, C) == 0:
                    return 0
        return 1

    result = apef_rec(E, Q, EP, F, Q0, Z0, QF, pilha, C)

    if result == 0:  # Printa se foi sucesso ou fracasso
        print("Sucesso")
    else:
        print("Fracasso")
    return


# MAIN
apef_start(E, Q, EP, F, Q0, Z0, QF, C)
