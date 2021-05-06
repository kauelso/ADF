def resolveOp(stack,elem,opcodes,popped):
    if popped == '(' or ')': #se o operador for um parenteses
        stack.append(popped) #devolve o parenteses na stack
        stack.append(elem) #coloca o operador analisado na stack
    elif opcodes.index(elem) >= opcodes.index(popped): #caso seja um operador e com maior prioridade
        stack.append(popped) #coloca o operador retirado na stack
        stack.append(elem) #coloca o operador analisado na stack

def resolveLessOp(stack,elem,opcodes,output):
    if stack: #caso ainda haja stack
        for op in stack: #para cada operador na stack
            if op != '(' and op != ')' and opcodes.index(elem) < opcodes.index(op): #se o operador ainda tiver menos prioridade
                popped = stack.pop() #Faz o pop do operador atual
                output.append(popped) #coloca ele no output
            else:
                popped = stack.pop() #faz o pop do operador atual
                resolveOp(stack,elem,opcodes,popped) #trata ele
                break
    if not stack:
        stack.append(elem)

ex = "(a+(a.b))" #expressao de entrada

opcodes = ['+','.','*'] #operadores em ordem (menos relevante para o mais relevante)

exlist = ex[::-1] #inverter a string de entrada

output = [] #output stack
stack = [] #op stack

for elem in exlist: #Para cada elemento da entrada
    if elem in opcodes: #se um elemento for um operador
        if stack: #caso tenha algo na pilha
            popped = stack.pop() #da pop no elemento que esta na pilha
            if popped in opcodes and opcodes.index(elem) < opcodes.index(popped): #se o elemento retirado for um operador e tiver maior prioridade 
                output.append(popped) #coloca o elemento retirado no output no output
                resolveLessOp(stack,elem,opcodes,popped) #trata o elemento que ira ser colocado
            else:
                resolveOp(stack,elem,opcodes,popped)
        else:
            stack.append(elem)
    elif elem == ')':
        stack.append(elem)
    elif elem == '(':
        popped = stack.pop()
        output.append(popped)
        while popped != ')':
            popped = stack.pop()
            output.append(popped)
        output.pop()
    else:
        output.append(elem)

if stack:
    for elem in stack:
        output.append(elem)

output.reverse()
str1 = "".join(str(x) for x in output)
print(str1)
    



