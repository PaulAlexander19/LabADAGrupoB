## Calcular la complejidad del código de la función
## Autor: Luque Ccosi, Paul Alexander

def ejercicio12(n):
    i = 0
    while(i < n):               # O(n)
        j = 1
        while(j < n):          # O(log n)
            j = j * 2
        i = i + 1

    return i

print(ejercicio12(10))

    # Análisis personal
        # La complejidad es O(n*log(n)) por que el ciclo interno es O(log(n)) y el ciclo externo es O(n)
        # La complejidad es nlog(n) entonces O(nlog(n))

    
    ## Demostración en clase:
        # // (1) This repeats n times
        # // (2) and this inner loop n times * log(n)
        # // (3) and this statement n times * log(n)
        # // Adding them together n + 2 n * log(n)
        # // O(n log(n))

