## Calcular la complejidad del código de la función
## Autor: Luque Ccosi, Paul Alexander


def ejercicio6(n):
    p = 0
    i = 1
    while(p <= n):
        p = p + i
        i = i + 1

    return p

print(ejercicio6(10))


    # Análisis personal
        # la complejidad es de O(n^(1/2)) ya que en cada iteración en P se almacena la suma de los primeros "i" numeros
        #  y esto se rompe cuando la suma pasa n

    
    ## Demostración en clase:
        # // A6:
        # //  i       p
        # // ------------------------
        # //  1       0 + 1 = 1
        # //  2       1 + 2
        # //  3       1 + 2 + 3
        # //  4       1 + 2 + 3 + 4
        # //  .
        # //  .
        # //  .
        # //  k       1 + 2 + 3 + 4 + ... + k

        # // Assume k > n
        # // p = k * (k + 1) / 2
        # //               p > n
        # // k * (k + 1) / 2 > n
        # // k^2 > n
        # // k > sqrt(n)
        # // O(n^(1/2))
