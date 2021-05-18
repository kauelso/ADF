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
    success_trace = []

    def afne_rec(E, Q, F, Q0, QF, C):  # Função para a recursão

        # Verifica de começo se a cadeia é vazia, já resolvendo caso comecar o automato com uma cadeia vazia
        if len(C) == 0:
            if Q0 in QF:
                trace.append([C+" ","Fim da recursao","Possiveis: []", "Cadeia Aceita"])
                return 0
            else:
                # Tratamento quando a C termina e ainda existe cadeia vazia possiveis na função
                for var in range(0, len(F)):
                    if F[var][0] == Q0 and F[var][1] == '':
                        for est in range(0, len(F[var][2])):
                            if afne_rec(E, Q, F, F[var][2][est], QF, C) == 0:  # recursão
                                return 0
                trace.append([C+" ","Fim da recursao","Possiveis: []", "Cadeia rejeitada, indo para outro caminho"])
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
                        print(f"Lendo: "+Q0+" em "+C[0])
                        print(f"Possiveis: {F[index][2]}")
                        print(f"indo para: " + F[index][2][est])
                        trace.append([C[1:]+" ",f"Lendo: "+Q0+" em "+C[0],f"Possiveis: {F[index][2]}",f"indo para: " + F[index][2][est]])
                        if afne_rec(E, Q, F, F[index][2][est], QF, C[1:]) == 0:  # recursão
                            return 0
                if F[index][1] == '':   # Encontra cadeia vazia na função
                    func = True
                    for est in range(0, len(F[index][2])):
                        print("Lendo: "+Q0 + " em transicao vazia")
                        print(f"Possiveis: {F[index][2]}")
                        print(f"Indo para: " + F[index][2][est])
                        trace.append([C+" ",f"Lendo: "+Q0+" em transicao vazia",f"Possiveis: {F[index][2]}",f"indo para: " + F[index][2][est]])
                        if afne_rec(E, Q, F, F[index][2][est], QF, C) == 0:  # recursão
                            return 0

        if func == False:
            return 1

    result = afne_rec(E, Q, F, Q0, QF, C)
    result_str = ""
    if result == 0:  # Printa se foi sucesso ou fracasso
        print("Sucesso")
        result_str = "Sucesso"
    else:
        print("Fracasso")
        result_str = "Fracasso"
    jsondata = {
        'steps':trace,
        'result':result_str
    }

    with open('AFNE/AFNE_automata_result.json','w') as write_file:
        json.dump(jsondata,write_file)
    return
