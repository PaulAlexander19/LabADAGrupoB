## Algoritmo de busqueda binaria
## Autor: Luque Ccosi Paul Alexander

def binarySearch(numbers, numberToFind):
    ## Inicializamos los valores de inicio y final
    ## verificamos que el numero a buscar sea menor que el final
    L = 0
    R = len(numbers) - 1
    
    while L <= R:
        mid = (L + R) // 2
        if numbers[mid] == numberToFind:
            return mid
        elif numbers[mid] < numberToFind:
            L = mid + 1
        else:
            R = mid - 1
    return -1 


## casos de prueba para el algoritmo de busqueda binaria
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binarySearch(numbers, 3))     ## devuelve 2
print(binarySearch(numbers, -1))    ## devuelve -1