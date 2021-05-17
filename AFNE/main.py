import ER_conver_AFNE as ER_AFNE
import infix_to_prefix as intp
import json
import AFNE as afne

def to_tuple(f):
    aux = [tuple(elem) for elem in f]
    return aux

print("Expressao que sera convertida: ")

exp = "((10)+(005)+2+123)"
exp = intp.convert(exp)
print(exp)
ER_AFNE.convert(exp)
# MAIN
print("Cadeia para ser calculada")

C = input()


with open('AFNE/AFNE_automata.json','r') as json_file:
    AFNjson = json.load(json_file)


E = AFNjson['E']  # Simbolos de entrada
Q = AFNjson['Q']  # Lista de estados
F = to_tuple(AFNjson['F'])  # Função de transição (Lista de tuplas) - [(Estado atual, simbolo, proximo estado),...]
Q0 = AFNjson['Q0']  # Estado inicial
QF = AFNjson['QF']  # Lista de estados finais

afne.afne_start(E, Q, F, Q0, QF,C)
