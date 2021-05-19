import json


def rem_rep(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    return l


def cria_automato(C, aut):
    i = aut * 2
    E = C
    Q = ['q'+str(i), 'q'+str(i+1)]
    F = [('q'+str(i), C, ['q'+str(i+1)])]
    Q0 = 'q'+str(i)
    QF = ['q'+str(i+1)]
    aut = aut + 1
    return E, Q, F, Q0, QF, aut


def cria_automato_vazio(aut):
    i = aut * 2
    E = ''
    Q = ['q'+str(i), 'q'+str(i+1)]
    F = [('q'+str(i), '', ['q'+str(i+1)])]
    Q0 = 'q'+str(i)
    QF = ['q'+str(i+1)]
    aut = aut + 1
    return E, Q, F, Q0, QF, aut


def concat_automato(E1, Q1, F1, Q01, QF1, E2, Q2, F2, Q02, QF2):
    E = E1+E2
    E = ''.join(rem_rep(E))
    Q = Q1+Q2
    F = F1 + [(QF1[0], "", [Q02])] + F2
    Q0 = Q01
    QF = QF2
    return E, Q, F, Q0, QF


def uniao_automato(E1, Q1, F1, Q01, QF1, E2, Q2, F2, Q02, QF2, aut):
    i = aut * 2
    E = E1+E2
    E = ''.join(rem_rep(E))
    Q = ['q'+str(i)] + Q1 + Q2 + ['q'+str(i+1)]
    F = [('q'+str(i), "", [Q01]), ('q'+str(i), "", [Q02])] + F1 + \
        F2 + [(QF1[0], "", ['q'+str(i+1)]), (QF2[0], "", ['q'+str(i+1)])]
    Q0 = 'q'+str(i)
    QF = ['q'+str(i+1)]
    aut = aut + 1
    return E, Q, F, Q0, QF, aut


def fecha_automato(E1, Q1, F1, Q01, QF1, aut):
    i = aut * 2
    E = E1
    Q = ['q'+str(i)] + Q1 + ['q'+str(i+1)]
    F = [('q'+str(i), "", ['q'+str(i+1)]), ('q'+str(i), "", [Q01])] + \
        F1 + [(QF1[0], "", [Q01]), (QF1[0], "", ['q'+str(i+1)])]
    Q0 = 'q'+str(i)
    QF = ['q'+str(i+1)]
    aut = aut + 1
    return E, Q, F, Q0, QF, aut


def convert(cad):
    cadeia = []
    pilha = []
    aut = 0    # Contador para o numero de estados criados para automatos (/2)

    for i in range(0, len(cad)):   # Coloca a cadeia em uma lista, para ser usada com pilha
        cadeia.append(cad[i])

    for j in range(0, len(cadeia)):
        op = cadeia.pop()

        if op == '+' or op == '.' or op == '*':
            if op == '*':
                E = pilha.pop()
                Q = pilha.pop()
                F = pilha.pop()
                Q0 = pilha.pop()
                QF = pilha.pop()
                E, Q, F, Q0, QF, aut = fecha_automato(E, Q, F, Q0, QF, aut)
                pilha.append(QF)
                pilha.append(Q0)
                pilha.append(F)
                pilha.append(Q)
                pilha.append(E)

            if op == '.':
                E = pilha.pop()
                Q = pilha.pop()
                F = pilha.pop()
                Q0 = pilha.pop()
                QF = pilha.pop()
                E1 = pilha.pop()
                Q1 = pilha.pop()
                F1 = pilha.pop()
                Q01 = pilha.pop()
                QF1 = pilha.pop()
                E, Q, F, Q0, QF = concat_automato(
                    E, Q, F, Q0, QF, E1, Q1, F1, Q01, QF1)
                pilha.append(QF)
                pilha.append(Q0)
                pilha.append(F)
                pilha.append(Q)
                pilha.append(E)

            if op == '+':
                E = pilha.pop()
                Q = pilha.pop()
                F = pilha.pop()
                Q0 = pilha.pop()
                QF = pilha.pop()
                E1 = pilha.pop()
                Q1 = pilha.pop()
                F1 = pilha.pop()
                Q01 = pilha.pop()
                QF1 = pilha.pop()
                E, Q, F, Q0, QF, aut = uniao_automato(
                    E, Q, F, Q0, QF, E1, Q1, F1, Q01, QF1, aut)
                pilha.append(QF)
                pilha.append(Q0)
                pilha.append(F)
                pilha.append(Q)
                pilha.append(E)

        else:
            if op == 'e':
                E, Q, F, Q0, QF, aut = cria_automato_vazio(aut)
                pilha.append(QF)
                pilha.append(Q0)
                pilha.append(F)
                pilha.append(Q)
                pilha.append(E)
            else:
                E, Q, F, Q0, QF, aut = cria_automato(op, aut)
                pilha.append(QF)
                pilha.append(Q0)
                pilha.append(F)
                pilha.append(Q)
                pilha.append(E)

    # A ordem é [QF, Q0, F, Q, E], para extrair mais facil é so dar pilha.pop para os json usando a ordem inversa :)
    pilha.reverse()

    jsondata = {
        'E': pilha[0],
        'Q': pilha[1],
        'Q0': pilha[3],
        'F': pilha[2],
        'QF': pilha[4]
    }

    with open('AFNE/AFNE_automata.json', 'w') as write_file:
        json.dump(jsondata, write_file)
