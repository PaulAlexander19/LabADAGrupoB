## Calcular la complejidad del código de la función
## Autor: Luque Ccosi, Paul Alexander

def ejercicio2(n):
    i = n
    while(i > 0):       #O(n)
        i = i - 1   # O(2)

    return i

print(ejercicio2(10))

    # Análisis personal
        # la complejidad temporal de este algoritmo es O(n) 
        # porque el bucle se ejecuta n veces.

    ## Demostración en clase:
        #la demostracion es la misma que el ejercicio 1, solo que
        # en este caso se utiliza una variable i que se incrementa

