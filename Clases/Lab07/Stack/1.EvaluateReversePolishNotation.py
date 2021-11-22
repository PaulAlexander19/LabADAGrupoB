#!/usr/bin/python

## NAME: Evaluate Reverse Polish Notation
## ALUMNO: Luque Ccosi Paul Alexander
## DESCRIPCION: Evaluar si una cadena de string cumple con la notacion de Polish y si cumple retornar el resultado


## Metodos para realizar las operaciones
def suma (numa, numb):
    return numa + numb

def resta (numa, numb):
    return numa - numb

def mul (numa, numb):
    return numa * numb

def div (numa, numb):
    return numa // numb

## Algoritmo 
def polishNotation(entrada):
    simbolos = "+-*/"
    s = []
    listData = entrada.split(" ")
    for  i in listData:  ## Separamos en una lista
        if (i in simbolos):
            operandoB = s.pop()
            operandoA = s.pop()
            if (i == "+"):
                s.append(suma(operandoA, operandoB))
            elif (i == "-"):
                s.append(resta(operandoA, operandoB))
            elif (i == "*"):
                s.append(mul(operandoA, operandoB))
            else:
                s.append(div(operandoA, operandoB))
            
        else:
            s.append(int(i))
            continue
            
    return s[0]


## Casos de prueba

entrada = "2 1 + 3 *"
print("Entrada :" + entrada)
print(polishNotation(entrada))

entrada = "4 13 5 / +"
print("Entrada :" + entrada)
print(polishNotation(entrada))

entrada = "10 6 9 3 + -11 * / * 17 + 5 +"
print("Entrada :" + entrada)
print(polishNotation(entrada))