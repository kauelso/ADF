import tkinter as tk
import json
import AFD
import AFDresultsGUI


def to_tuple(f):
    aux = [tuple(elem) for elem in f]
    return aux

def format_transition(t):
    convert = lambda x: "δ=("+str(x[0])+","+str(x[1])+")="+str(x[2])
    aux = [convert(elem) for elem in t]
    return aux

with open('AFNjson.json','r') as json_file:
    AFDjson = json.load(json_file)

E = AFDjson['E']  # Simbolos de entrada
Q = AFDjson['Q']  # Lista de estados
F = to_tuple(AFDjson['F'])  # Função de transição (Lista de tuplas) - [(Estado atual, simbolo, proximo estado),...]
Q0 = AFDjson['Q0']  # Estado inicial
QF = AFDjson['QF']  # Lista de estados finais


window = tk.Tk()
label = tk.Label(text="Cadeia")
entry = tk.Entry()
Elabel = tk.Label(text="Σ={" + E + "}")
Qlabel = tk.Label(text="Q={" + str(Q) + "}")


label.pack()
entry.pack()
Elabel.pack()
Qlabel.pack()


submit = tk.Button(window, text ="Submit")
#show = tk.Button(window, text ="output")

submit.pack()
#show.pack()

window.mainloop()


