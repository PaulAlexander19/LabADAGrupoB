## Calcular la complejidad del código de la función
## Autor: Luque Ccosi, Paul Alexander


def ejercicio4(n):
    i = 0                   # contador
    while(i < n):           # o(n)
        j = 0               # contador
        while(j < n):       # o(n)
            j = j+1         # incremento j
        i = i+1             # incremento i

    return i
    
print(ejercicio4(13))

    # Análisis personal
        # La complejidad temporal de este algoritmo es O(n^2) 
        # porque el bucle se ejecuta n veces y dentro de cada bucle se ejecuta n veces.

    ## Demostración en clase:
        #     // A4: O(n^2)
        #     for (i = 0; i < n; i++) {       // n + 1
        #         for (j = 0; j < n; j++) {   // n * (n + 1)
        #             statement;              // n * n
        #             cout << "i" << '\n';
        #     }
        # }

