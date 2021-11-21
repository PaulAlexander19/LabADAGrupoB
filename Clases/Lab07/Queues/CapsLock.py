#!/usr/bin/python

# Luque Ccosi Paul Alexander

## Ejerccio 3 usando colas para poner en mayuscula segun el los caracteres del ACTIVATE o DESACTIVATE

from collections import deque

def capsLock(str):
    activate = "@"
    desactivate = "$"
    q = deque()
    flag = False
    for i in str:   
        if(i in activate):
            flag = True
            continue
        elif (i in desactivate):
            flag = False
            continue

        # Agregar de acuerdo a la si esta activado o no
        if(flag):
            q.append(i.upper())
        else:
            q.append(i)


    return q

## CASOS DE PRUEBA
text = "abc$d@ef$g$"
r = capsLock(text)
resultado = ""
for i in r:
    resultado += i
print("Texto: " + text)
print("Resultado Final: "+resultado)

print("-------------------")

text = "hola@yo$tu"
r = capsLock(text)
resultado = ""
for i in r:
    resultado += i

print("Texto: " + text)
print("Resultado Final: "+resultado)