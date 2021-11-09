## Calcular la complejidad del código de la función
## Autor: Luque Ccosi, Paul Alexander


def ejercicio3(n):
    i = 0           # Contador de iteraciones
    while(i < n):   # Mientras i sea menor que n o(n)
        i = i + 5   # Incremento de i en 5
    return i        # Retorno de i

print(ejercicio3(13))

    # Análisis personal
        # la complejidad temporal de este algotimo es O(n/5) 
        # pero se pude trabajar con O(n).



