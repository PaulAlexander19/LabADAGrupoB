## Calcular la complejidad del código de la función
## Autor: Luque Ccosi, Paul Alexander

def ejercicio11(n):
    p = 0
    i = 1
    while(i < n):   # O(log(n))      
        p = p + 1
        i = i * 2

    j = 1
    while(j < p):   # O(log(log(n)))
        j = j * 2

    return p

print(ejercicio11(10))

    # Análisis personal
        # La complejidad es log(log(n)) es un ejecto cadena, el primer buble ya lo resolvimos
        # y sale log(p) en el segundo bucle es la misma idea log(p), seria log(log(p))

    
    ## Demostración en clase:
        # // A11:
        # p = 0
        # // (2)
        # for (i = 1; i < n; i = i * 2) {
        #     p++;                    // p = log(n)
        # }

        # // (1)
        # for (j = 1; j < p; j = j * 2) {
        #     statement;              // log(p)
        # }

        # // So, we have log(p) and p = log(n)
        # // replacing log log(n)
        # // O(log log(n))

