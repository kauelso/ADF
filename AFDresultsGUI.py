import tkinter as tk
import json

def to_tuple(f):
    aux = [tuple(elem) for elem in f] 
    return aux

def format_transition(t):
    convert = lambda x: "δ=("+str(x[0])+","+str(x[1])+")="+str(x[2])
    aux = convert(t)
    return aux

def executar(window,contador,steps,state):
    print(len(steps))
    if contador[0] < len(steps):
        stepslabel = tk.Label(window,text= f"Caracter: {steps[contador[0]][1]}  Estado atual: {steps[contador[0]][0]}")
        stepslabel.pack()

        stepslabel = tk.Label(window,text=str(format_transition(steps[contador[0]])))
        stepslabel.pack()
    else:
        statelabel = tk.Label(window,text= state)
        statelabel.pack()

    contador[0] = contador[0] + 1

def GUIstart(cadeia):

    with open('ADFresults.json','r') as json_file:
        ADF = json.load(json_file)
    steps = to_tuple(ADF['steps'])  # Lista de tuplas executadas - [(Estado atual, simbolo, proximo estado),...]
    state = ADF['state']

    contador = [0]

    window = tk.Tk()
    window.geometry("500x500")
    frame = tk.Frame(window,width="500",height="500")
    frame.pack()
    #swin = ScrolledWindow(frame, width=500, height=500)
    #swin.pack()
    label = tk.Label(frame,text= f"Cadeia: {cadeia}")
    label.pack()
    #label.grid(row=1, column=1)

    avancar = tk.Button(frame, text ="Avançar", command = lambda: executar(frame,contador,steps,state))
    avancar.pack()

    # Enter into eventloop <- this will keep
    # running your application, until you exit
    window.mainloop()