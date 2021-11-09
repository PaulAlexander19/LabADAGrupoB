## Calcular la complejidad del código de la función
## Autor: Luque Ccosi, Paul Alexander

def ejercicio8(n):
    i = n
    while(i >= 1):
        i = i/2

    return i

print(ejercicio8(10))

    # Análisis personal
        # La complejidad es de log_2(n) ya que i tiene la forma (n/2^k)
        # y para que se rompa la condicion k tiene que ser log_2(n)

    
    ## Demostración en clase:
        # //  i
        # // ------------------------
        # //  n
        # //  n / 2
        # //  n / 2^2
        # //  n / 2^3
        # //  .
        # //  .
        # //  .
        # //  n / 2^k

        # // Assume that i < 1
        # // Therefore n / 2^k < 1
        # //           n / 2^k = 1
        # //                 n = 2^k
        # //                 k = log_2(n)
        # // A8: O(log_2(n))

