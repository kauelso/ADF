def cria_automato(C, aut):
    i = aut * 2
    E = C
    Q = ['q'+str(i), 'q'+str(i+1)]
    F = [('q'+str(i), C, ['q'+str(i+1)])]
    Q0 = 'q'+str(i)
    QF = ['q'+str(i+1)]
    return E, Q, F, Q0, QF


def concat_automato(E1, Q1, F1, Q01, QF1, E2, Q2, F2, Q02, QF2):
    E = E1+E2
    Q = Q1+Q2
    F = F1 + [(QF1[0], "", [Q02])] + F2
    Q0 = Q01
    QF = QF2
    return E, Q, F, Q0, QF


def uniao_automato(E1, Q1, F1, Q01, QF1, E2, Q2, F2, Q02, QF2, aut):
    i = aut * 2
    E = E1+E2
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
    pilha = []
    count = 0  # Contador para o numero de automatos (max = 2)
    aut = 0    # Contador para o numero de estados criados para automatos (/2)

    for i in range(0, len(cad)):
        if cad[i] == '+' or cad[i] == '.' or cad[i] == '*':  # Verifica se foi lido um operador
            pilha.append(cad[i])
        else:
            if count == 0:
                E1, Q1, F1, Q01, QF1 = cria_automato(cad[i], aut)
                count = count + 1
                aut = aut + 1
                if pilha[-1] == '*':
                    E1, Q1, F1, Q01, QF1, aut = fecha_automato(
                        E1, Q1, F1, Q01, QF1, aut)
            elif count == 1:
                E2, Q2, F2, Q02, QF2 = cria_automato(cad[i], aut)
                count = count + 1
                aut = aut + 1

                while count == 2:
                    op = pilha.pop()
                    if op == '*':
                        E2, Q2, F2, Q02, QF2, aut = fecha_automato(
                            E2, Q2, F2, Q02, QF2, aut)
                    if op == '.':
                        E1, Q1, F1, Q01, QF1 = concat_automato(
                            E1, Q1, F1, Q01, QF1, E2, Q2, F2, Q02, QF2)
                        count = 1
                        if len(pilha) > 0 and pilha[-1] == '*':
                            E1, Q1, F1, Q01, QF1, aut = fecha_automato(
                                E1, Q1, F1, Q01, QF1, aut)
                    if op == '+':
                        E1, Q1, F1, Q01, QF1, aut = uniao_automato(
                            E1, Q1, F1, Q01, QF1, E2, Q2, F2, Q02, QF2, aut)
                        count = 1
                        if len(pilha) > 0 and pilha[-1] == '*':
                            E1, Q1, F1, Q01, QF1, aut = fecha_automato(
                                E1, Q1, F1, Q01, QF1, aut)

    print(E1)
    print(Q1)
    print(F1)
    print(Q01)
    print(QF1)
    print('== == == == == ')


cadeia = '+*.011'  # (a+b).c
convert(cadeia)
