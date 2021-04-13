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

with open('AFDjson.json','r') as json_file:
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

def StartAFD(E,Q,F,Q0,QF):
    C = entry.get()
    AFD.adf_start(E,Q,F,Q0,QF,C)
    AFDresultsGUI.GUIstart(C)



label.pack()
entry.pack()
Elabel.pack()
Qlabel.pack()
    
# for elem in format_transition(F):
#     tamanho = len(F)
#     for 
#     Flabel = tk.Label(text= elem)
#     Flabel.pack()
indice = 0
scrollbar = tk.Scrollbar(window)
scrollbar.pack( side = "right", fill = "y" )
transicoes = format_transition(F)
mylist = tk.Listbox(window, yscrollcommand = scrollbar.set )
for elem in transicoes:
     mylist.insert(indice,elem)
     indice = indice + 1

mylist.pack( side = "bottom", fill = "both" )
scrollbar.config( command = mylist.yview )

#Flabel = tk.Label(text=str(format_transition(F)))
Q0label = tk.Label(text="q0={" + str(Q0) + "}")
QFlabel = tk.Label(text="F={" + str(QF) + "}")
#Flabel.pack()
Q0label.pack()
QFlabel.pack()


submit = tk.Button(window, text ="Submit", command = lambda: StartAFD(E,Q,F,Q0,QF))
#show = tk.Button(window, text ="output", command = lambda: AFDresultsGUI.GUIstart(cadeia))

submit.pack()
#show.pack()

# Enter into eventloop <- this will keep
# running your application, until you exit
window.mainloop()