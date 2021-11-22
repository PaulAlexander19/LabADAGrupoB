#!/usr/bin/python

# ALUMNO: Luque Ccosi Paul Alexander
## DESCRIPCION: Ejerccio 3 usando colas para poner en mayuscula segun el los caracteres del ACTIVATE o DESACTIVATE

from collections import deque

def capsLock(str):
    resul = ""      ## Donde se almacenará el resultado
    activate = "@"      
    desactivate = "$"
    q = deque()
    flagActivate = None ## en un inicio no esta activado ni desactivado, para que ingrese tanto mayuscula como miniscula
    for i in str:
        ## Conversion del buffer o salida del  buffe
        if(i in activate):
            if(flagActivate == None or flagActivate == False):
                q = deque([x.upper() for x in q])  ## Convirtiendo el buffer en matusculas
                flagActivate = True  ## cambiando la bandera
            else:
                q = deque([x.lower() for x in q])  ## Convirtiendo el buffer en matusculas
                flagActivate = False  ## cambiando la bandera
        elif(i in desactivate): ## liberamos el buffer
            for i in range(len(q)):
                resul += q.popleft()
        else: ## Ingresamos un valor
            ## Ingresamos segun el estado de flagActivate "@"
            if(flagActivate == False):
                q.append(i.lower())
            elif(flagActivate == True):
                q.append(i.upper())
            else: ## Agreamos si no esta actvado ni descatiavdo "@"
                q.append(i)
    
    ## liberamos el resto del buffer
    for i in range(len(q)):
        resul += q.popleft() ## sacamos un elemento por la izquierda
    
                    


    return resul

## CASOS DE PRUEBA
text = "abc$d@ef$@g$"
print("Texto: " + text)
print("Resultado Final: "+capsLock(text))

print("-------------------")

text = "pro@band$o@$"
print("Texto: " + text)
print("Resultado Final: "+capsLock(text))

text = "pro@band$o@"
print("Texto: " + text)
print("Resultado Final: "+capsLock(text))