## Calcular la complejidad del código de la función
## Autor: Luque Ccosi, Paul Alexander


def ejercicio5(n):
    i = 0
    while(i < n):
        j = 0
        while(j < i):
            i = j + 1
        i = i + 1



    # Análisis personal
        #  la complejidad del algoritmo es o(n^2) ya que el buble superior se ejecuta n veces
        #  pero el buble interior se ejecuta la cantidad de i veces en un punto llegara que i sera cerca a n y por lo tanto
        #  j recorrera n veces
    
    ## Demostración en clase:
        # // A5:
        # // Tracing the values of the variables
        # //  i   j      no of times
        # // ------------------------
        # //  0   0 ❌     0
        # // ------------------------
        # //  1   0 ✔️     1
        # //      1 ❌
        # // ------------------------
        # //  2   0 ✔️     2
        # //      1 ✔️
        # //      2 ❌
        # // ------------------------
        # //  .
        # //  .
        # //  .
        # // ------------------------
        # //  n             n

        # // 1 + 2 + 3 + ... + n = n * (n + 1) / 2
        # // O(n^2)
