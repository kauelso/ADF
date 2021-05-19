def normalizeExp(str1):
    out = ""
    for elem in str1:
        if elem in ["+", "."]:
            out = out + elem
        elif out != "":
            aux = out[-1]
            if aux in ["+", "."] or aux == "(":
                out = out + elem
            elif elem == "*":
                out = out + elem
            elif elem == ")" and aux == ")":
                out = out+elem
            elif aux == ")" and elem == "(":
                out = out + '.'
                out = out + elem
            elif elem == ")" and aux not in ["+", "."] and aux not in ["(", ")"]:
                out = out+elem
            else:
                out = out + '.'
                out = out + elem
        else:
            out = out+elem
    return out


def resolveOp(stack, elem, opcodes, popped):
    if popped == '(' or ')':  # se o operador for um parenteses
        stack.append(popped)  # devolve o parenteses na stack
        stack.append(elem)  # coloca o operador analisado na stack
    # caso seja um operador e com maior prioridade
    elif opcodes.index(elem) >= opcodes.index(popped):
        stack.append(popped)  # coloca o operador retirado na stack
        stack.append(elem)  # coloca o operador analisado na stack


def resolveLessOp(stack, elem, opcodes, output):
    if stack:  # caso ainda haja stack
        stack_aux = stack.copy()
        stack_aux.reverse()
        for op in stack_aux:  # para cada operador na stack
            if op == "(" or op == ")":
                stack.append(elem)
                break
            # se o operador ainda tiver menos prioridade
            elif opcodes.index(elem) < opcodes.index(op):
                popped = stack.pop()  # Faz o pop do operador atual
                output.append(popped)  # coloca ele no output
            else:
                stack.append(elem)
                break
    if not stack:
        stack.append(elem)


def convert(ex):
    # operadores em ordem (menos relevante para o mais relevante)
    opcodes = ['+', '.', '*']

    exlist = normalizeExp(ex)[::-1]  # inverter a string de entrada

    output = []  # output stack
    stack = []  # op stack

    for elem in exlist:  # Para cada elemento da entrada
        if elem in opcodes:  # se um elemento for um operador
            if stack:  # caso tenha algo na pilha
                popped = stack.pop()  # da pop no elemento que esta na pilha
                # se o elemento retirado for um operador e tiver maior prioridade
                if popped in opcodes and opcodes.index(elem) < opcodes.index(popped):
                    # coloca o elemento retirado no output
                    output.append(popped)
                    # trata o elemento que ira ser colocado
                    resolveLessOp(stack, elem, opcodes, output)
                else:
                    # Se o operador tiver maior precedencia ou o top da pilha nao for um operador ele é tratado nessa func
                    resolveOp(stack, elem, opcodes, popped)
            else:
                # se nao tiver nada na pilha, empilha o operador
                stack.append(elem)
        elif elem == ')':  # se  for um parenteses fechado
            stack.append(elem)  # empilha o parenteses
        elif elem == '(':  # se for um parenteses aberto
            # remove os elementos e coloca no output ate achar o parenteses fechado
            popped = stack.pop()
            output.append(popped)
            while popped != ')':
                popped = stack.pop()
                output.append(popped)
            output.pop()
        else:  # caso nao seja nenhum outro caso ele sera um operador e deve ir para o output
            output.append(elem)

    while stack:  # por fim, desempilha toda a pilha
        elem = stack.pop()
        output.append(elem)

    output.reverse()  # inverte o array de output
    str1 = "".join(str(x) for x in output)  # transforma o array em uma string
    return str1
