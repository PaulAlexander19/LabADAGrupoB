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
    number = ""
    flag_antes = False
    for  i in entrada:
        
        
        # print(i)
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
            if(i == " " and flag_antes == False):
                # print("number: "+number)
                s.push(int(number))
                number = ""   
                continue
            else:
                flag_antes = False
                number = str(number) + str(i)
            
    return s.top()


## Casos de prueba
simbolos = "+-*/"


# entrada = "2 1 + 3 *"
# print("Entrada :" + entrada)
# print(polishNotation(entrada, simbolos))

# entrada = "4 13 5 / +"
# print("Entrada :" + entrada)
# print(polishNotation(entrada, simbolos))

entrada = "10 6 9 3 + -11 * / * 17 + 5 +"
print("Entrada :" + entrada)
print(polishNotation(entrada, simbolos))