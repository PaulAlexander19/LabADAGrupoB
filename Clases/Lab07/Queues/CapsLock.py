#!/usr/bin/python

# Luque Ccosi Paul Alexander

## Ejerccio 3 usando colas para poner en mayuscula

from collections import deque

def capsLock(str):
    activate = "@"
    desactivate = "$"
    q = deque()
    print(str)
    flag = False
    for i in str:   
        if(i in activate):
            falg = True
            continue
        elif (i in desactivate):
            falg = False
            continue

        # Agregar de acuerdo a la si esta activado o no
        if(flag):
            q.append(i.upper())
            print(q)
        else:
            q.append(i)
            print(q)

    return q

text = "hola@yo$tu"

r = capsLock(text)
print(r)
