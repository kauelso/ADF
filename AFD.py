import json

def pertence(E, t):  # Verifica se o teste pertence aos simbolos de entrada
    if t in E:
        return 0
    else:
        return 1

class data: #Objeto que guarda a execução do automato
    steps = []
    state = ""

def adf_start(E,Q,F,Q0,QF,C):
    jsonData = data()
    jsonData.steps = [] #Zera os passos do automato
    Eatual = Q0  # Eatual representa o estado atual
    i = 0  # i representa i indice da cadeia de teste
    invalido = False

    while 1:
        if pertence(E, C[i]) == 1:  # Verifica se a entrada atual pertence ao alfabeto
            jsonData.steps.append([Eatual,C[i],"Simbolo fora do alfabeto"])
            jsonData.state = "REJEITADA"
            invalido = True #Cadeia invalida
            break

        # Procura alguma função com o mesmo estado que o atual e o mesmo simbolo que a cadeia
        for index in range(0, len(F)):
            erro = 1
            if (F[index][0] == Eatual) and (F[index][1] == C[i]):
                Eatual = F[index][2]  # proximo estado
                jsonData.steps.append([F[index][0],F[index][1],F[index][2]]) # Guarda transicao executada
                i = i+1  # proximo elemento da cadeia de teste
                erro = 0  # Controle para o loop
                break

        if erro == 1:  # Verifica se existe nas funções a cadeia e o estado
            jsonData.steps.append([Eatual,C[i],"Nenhuma funcao de transicao correspondente"])
            jsonData.state = f"REJEITADA"
            invalido = True #Cadeia innvalida
            break

        if i == len(C):  # Verifica se toda a cadeia de teste ja passou
            break

    if Eatual in QF and invalido is False:  # Verifica se a cadeia foi aceitada ou não
        data.state = "ACEITA!" # Cadeia do automato aceita
    elif invalido is False:
        jsonData.state = "REJEITADA!" # Cadeia do automato rejeitada
        Efinal = str(QF)[1:-1]

    jsonString = { # Formatacao do JSON de resultados
        'steps':jsonData.steps,
        'state':jsonData.state
        }

    with open("ADFresults.json","w") as write_file:
        json.dump(jsonString,write_file)


# Saida:
# a quíntupla fornecida na entrada e para cadeia testada
# a cadeia testada
# ACEITA ou REJEITADA
# Passo a passo do funcionamento de cada cadeia, mostrando o que éfeito a cada posição da cadeia
