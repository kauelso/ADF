import tkinter as tk
import json

def to_tuple(f):
    aux = [tuple(elem) for elem in f] 
    return aux

def format_transition(t):
    convert = lambda x: "δ=("+str(x[0])+","+str(x[1])+")="+str(x[2])
    aux = convert(t)
    return aux


def executar(cadeia,window,contador,steps,state,label,slabel,Clabel):
    if contador[0] < len(steps):
        Clabel.config(text= f"Cadeia lida: {cadeia[0:contador[0]+1]}")
        Clabel.update()

        label.config(text= f"Caracter: {steps[contador[0]][1]}  Estado atual: {steps[contador[0]][0]}")
        label.update()

        slabel.config(text = str(format_transition(steps[contador[0]])))
        slabel.update()
    else:
        statelabel = tk.Label(window,text= state)
        statelabel.pack()

    contador[0] = contador[0] + 1

def GUIstart(cadeia):

    with open('AFN/AFNresults.json','r') as json_file:
        ADF = json.load(json_file)
    steps = to_tuple(ADF['steps'])  # Lista de tuplas executadas - [(Estado atual, simbolo, proximo estado),...]
    state = ADF['state']

    contador = [0]

    window = tk.Tk()
    window.geometry("300x300")
    frame = tk.Frame(window,width="300",height="300")
    frame.pack()
    label = tk.Label(frame,text= f"Cadeia: {cadeia}")
    label.pack()
    slabel = tk.Label(frame)
    slabel.pack()
    stlabel = tk.Label(frame)
    stlabel.pack()
    Clabel = tk.Label(frame)
    Clabel.pack()
    avancar = tk.Button(frame, text ="Avançar", command = lambda: executar(cadeia,frame,contador,steps,state,slabel,stlabel,Clabel))
    avancar.pack()


    # Enter into eventloop <- this will keep
    # running your application, until you exit
    window.mainloop()