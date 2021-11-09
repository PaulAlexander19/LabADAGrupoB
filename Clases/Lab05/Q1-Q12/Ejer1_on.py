## Calcular la complejidad del código de la función
## Autor: Luque Ccosi, Paul Alexander

def ejercicio1 (n):
    # Q1: What is the time complexity of
    i = 0
    while (i < n):          # O(n)
        i = i + 1       # O(2)

    return i

print(ejercicio1(10))

    # Análisis personal
        # La complejidad temporal de este algoritmo es O(n) 
        # porque el bucle se ejecuta n veces.

    ## Demostración en clase:
        # A1: O(n)
        # for (i = 0; i < n; i++) {   // n + 1
        #     statement;               // n
        # }

