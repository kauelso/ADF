import tkinter as tk
import json

def to_tuple(f):
    aux = [tuple(elem) for elem in f]
    return aux

def format_transition(t):
    convert = lambda x: "δ=("+str(x[0])+","+str(x[1])+")="+str(x[2])
    aux = [convert(elem) for elem in t]
    return aux

with open('ADFjson.json','r') as json_file:
    ADF = json.load(json_file)

E = ADF['E']  # Simbolos de entrada
Q = ADF['Q']  # Lista de estados
F = to_tuple(ADF['F'])  # Função de transição (Lista de tuplas) - [(Estado atual, simbolo, proximo estado),...]
Q0 = ADF['Q0']  # Estado inicial
QF = ADF['QF']  # Lista de estados finais

window = tk.Tk()
label = tk.Label(text="Cadeia")
entry = tk.Entry()
Elabel = tk.Label(text="Σ={" + E + "}")
Qlabel = tk.Label(text="Q={" + str(Q) + "}")

label.pack()
entry.pack()
Elabel.pack()
Qlabel.pack()
    
for elem in format_transition(F):
    Flabel = tk.Label(text= elem)
    Flabel.pack()

Flabel = tk.Label(text=str(format_transition(F)))
Q0label = tk.Label(text="q0={" + str(Q0) + "}")
QFlabel = tk.Label(text="F={" + str(QF) + "}")


Q0label.pack()
QFlabel.pack()

# Enter into eventloop <- this will keep
# running your application, until you exit
window.mainloop()