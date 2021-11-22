## Ejercicio Backspace
## En una cola doblemente enlazada borrar el ultimo elemento si se ingresa un #
# Luque Ccosi Paul Alexander
from collections import deque

def Backspace(str):
    key = "#"
    d = deque()
    
    for i in str:
        if i == key:
            try:
                d.pop()
            except IndexError:
                pass
                print("Cola vacia no se borra nada")
        else:
            d.append(i)
            
    return "".join(d)


## Casos de prueba

text = "#abc#de##f#ghi#jklmn#op#"
print(text)
print(Backspace(text))