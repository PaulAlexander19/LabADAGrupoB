## Calcular la complejidad del código de la función
## Autor: Luque Ccosi, Paul Alexander

def ejercicio9(n):
    i = 0
    while(i*i < n):
        i = i + 1

    return i

print(ejercicio9(10))

    # Análisis personal
        # Para que el ciclo termine, tenemos que asumir que i^2 = n por lo que la complejidad es O(sqrt(n))

    
    ## Demostración en clase:
        # // Condition       i * i < n
        # // To finish       i * i >= n
        # // We assume that     i^2 = n
        # //                      i = sqrt(n)
        # // A9: O(sqrt(n))


