## Ejercicio Backspace

## DESCRIPCION: En una cola doblemente enlazada borrar el ultimo elemento si se ingresa un #
## Autor:  Luque Ccosi Paul Alexander
from collections import deque

def Backspace(str):
    key = "#"
    d = deque()
    
    for i in str:
        if i == key:
            try:
                d.pop()
            except IndexError: ## por si no hay elementos
                pass
                print("Cola vacia no se borra nada")
        else:
            d.append(i)
            
    return "".join(d) ## retornamos una cadena con los elementos de la cola d


## Casos de prueba

text = "#abc#de##f#ghi#jklmn#op#"
print(text)
print(Backspace(text))