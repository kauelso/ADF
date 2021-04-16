import tkinter as tk
import sys
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


def StartAFD(E,Q,F,Q0,QF,entry):
    C = entry.get()
    AFD.afd_start(E,Q,F,Q0,QF,C)
    AFDresultsGUI.GUIstart(C)

def StartAFDtoAFNGUI(E,Q,F,Q0,QF):

    window = tk.Tk()
    label = tk.Label(text="Cadeia")
    entry = tk.Entry()
    Elabel = tk.Label(text="Σ={" + E + "}")
    Qlabel = tk.Label(text="Q={" + str(Q) + "}")


    label.pack()
    entry.pack()
    Elabel.pack()
    Qlabel.pack()
        

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


    Q0label = tk.Label(text="q0={" + str(Q0) + "}")
    QFlabel = tk.Label(text="F={" + str(QF) + "}")

    Q0label.pack()
    QFlabel.pack()


    submit = tk.Button(window, text ="Submit", command = lambda: StartAFD(E,Q,F,Q0,QF,entry))


    submit.pack()

    window.mainloop()