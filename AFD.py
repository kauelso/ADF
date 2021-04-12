import sys


def pertence(E, t):  # Verifica se o teste pertence aos simbolos de entrada
    if t in E:
        return 0
    else:
        return 1


# Parte dos dados
E = 'ab'  # Simbolos de entrada
Q = ['q0', 'q1', 'q2', 'q3']  # Lista de estados
F = [("q0", "a", "q1"), ("q0", "b", "q2"), ("q1", "a", "q3"), ("q1", "b", "q2"), ("q2", "a", "q1"), ("q2", "b", "q3"),
     ("q3", "a", "q3"), ("q3", "b", "q3")]  # Função de transição (Lista de tuplas) - [(Estado atual, simbolo, proximo estado),...]
Q0 = 'q0'  # Estado inicial
QF = ['q3']  # Lista de estados finais
C = "ababaa"  # Cadeia de teste

#                      #
#  INICIO DO AUTOMATO  #
#                      #

Eatual = Q0  # Eatual representa o estado atual
i = 0  # i representa i indice da cadeia de teste

while 1:
    if pertence(E, C[i]) == 1:  # Verifica se a entrada atual pertence ao alfabeto
        print("Erro, simbolo não existe no alfabeto!")
        sys.exit()

    # Procura alguma função com o mesmo estado que o atual e o mesmo simbolo que a cadeia
    for index in range(0, len(F)):
        erro = 1
        if (F[index][0] == Eatual) and (F[index][1] == C[i]):
            print(f"Lendo '{C[i]}' no estado '{Eatual}'")  # Passos
            Eatual = F[index][2]  # proximo estado
            print(
                f"Função de Transição: ({F[index][0]},{F[index][1]}) = {F[index][2]}")  # Passos
            i = i+1  # proximo elemento da cadeia de teste
            erro = 0  # Controle para o loop
            break

    if erro == 1:  # Verifica se existe nas funções a cadeia e o estado
        print(
            f"Erro, estado atual {Eatual} ou cadeia de teste {C[i]} não correspondida nas funções")
        sys.exit()

    if i == len(C):  # Verifica se toda a cadeia de teste ja passou
        break

if Eatual in QF:  # Verifica se a cadeia foi aceitada ou não
    print("ACEITA!")
else:
    print("REJEITADA!")
    Efinal = str(QF)[1:-1]
    print(f"O estado final foi o '{Eatual}' e não o {Efinal}")

# Saida:
# a quíntupla fornecida na entrada e para cadeia testada
# a cadeia testada
# ACEITA ou REJEITADA
# Passo a passo do funcionamento de cada cadeia, mostrando o que éfeito a cada posição da cadeia
