from Stack import Stack
s = Stack()

def suma (numa, numb):
    return numa + numb

def resta (numa, numb):
    return numa - numb

def mul (numa, numb):
    return numa * numb

def div (numa, numb):
    return numa // numb

def polishNotation(entrada, simbolos):
    for  i in entrada.split():
        if(i in simbolos):
            flag_antes =   True
            operandoB = s.pop()
            operandoA = s.pop()
            if(i == "+"):
                s.push(suma(operandoA, operandoB))
            elif(i == "-"):
                s.push(resta(operandoA, operandoB))
            elif(i == "*"):
                s.push(mul(operandoA, operandoB))
            else:
                s.push(div(operandoA, operandoB))
            
        else:
            s.push(int(i))
            continue
            
    return s.top()


## Casos de prueba
simbolos = "+-*/"


entrada = "2 1 + 3 *"
print("Entrada :" + entrada)
print(polishNotation(entrada, simbolos))

entrada = "4 13 5 / +"
print("Entrada :" + entrada)
print(polishNotation(entrada, simbolos))

entrada = "10 6 9 3 + -11 * / * 17 + 5 +"
print("Entrada :" + entrada)
print(polishNotation(entrada, simbolos))