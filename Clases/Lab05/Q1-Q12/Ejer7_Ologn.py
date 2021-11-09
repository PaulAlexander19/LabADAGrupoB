## Calcular la complejidad del código de la función
## Autor: Luque Ccosi, Paul Alexander


def ejercicio7(n):
    i = 1
    while(i < n):
        i = i * 2

    return i

print(ejercicio7(10))

    # Análisis personal
        # El algoritmo tiene una complejidad de O(log_2(n)) ya que se ejecuta hasya
        # el paso 2^k entonces para que ya no se cumpla la condición es log_2(n)

    
    ## Demostración en clase:
        # // A7:
        # //  i
        # // ------------------------
        # //  1
        # //  1 * 2 = 2
        # //  2 * 2 = 2^2
        # //  2 * 2^2 = 2^3
        # //  .
        # //  .
        # //  .
        # //  2^k

        # // Assume i >= n
        # // Therefore i = 2^k
        # //      2^k >= n
        # //       2^k = n
        # //         k = log_2(n)
        # // O(log_2(n))

