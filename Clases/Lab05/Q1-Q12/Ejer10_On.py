## Calcular la complejidad del código de la función
## Autor: Luque Ccosi, Paul Alexander

def ejercicio10(n):
    i = 0
    while(i < n):
        i = i + 1

    j = 0
    while(j < n):
        j = j + 1

    return i

print(ejercicio10(10))

    # Análisis personal
        # la complejidad es O(n) porque en cada ciclo e O(n) y en total seria 2 * n

    
    ## Demostración en clase:
        # // A10: O(n)
        # for (i = 0; i < n; i++) {
        #     statement;          // n
        # }

        # for (j = 0; j < n; j++) {
        #     statement;          // n
        # }
        #   

