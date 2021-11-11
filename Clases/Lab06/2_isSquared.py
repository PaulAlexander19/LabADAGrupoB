## 1 Determianr si es el numero es cuadrado
## Autor: Luque Ccosi Paul Alexander

def isSquaredBinarySearch(number):
    ## es lo mismo que la busqueda binaria, pero ahora buscamos si es su raiz
    L = 0
    R = number - 1
    
    while L <= R:
        mid = (L + R) // 2
        option = mid * mid
        if option == number:
            return True
        elif option < number :
            L = mid + 1
        else:
            R = mid - 1
    return False


## casos de prueba para isSquaredBinarySearch
print("isSquaredBinarySearch(1):", isSquaredBinarySearch(1))
print("isSquaredBinarySearch(2):", isSquaredBinarySearch(2))
print("isSquaredBinarySearch(3):", isSquaredBinarySearch(3))
print("isSquaredBinarySearch(4):", isSquaredBinarySearch(4))
print("isSquaredBinarySearch(5):", isSquaredBinarySearch(5))
print("isSquaredBinarySearch(6):", isSquaredBinarySearch(6))
print("isSquaredBinarySearch(7):", isSquaredBinarySearch(7))
print("isSquaredBinarySearch(8):", isSquaredBinarySearch(8))
print("isSquaredBinarySearch(9):", isSquaredBinarySearch(9))
print("isSquaredBinarySearch(10):", isSquaredBinarySearch(10))
print("isSquaredBinarySearch(11):", isSquaredBinarySearch(11))
print("isSquaredBinarySearch(12):", isSquaredBinarySearch(12))
print("isSquaredBinarySearch(13):", isSquaredBinarySearch(13))
print("isSquaredBinarySearch(14):", isSquaredBinarySearch(14))
print("isSquaredBinarySearch(15):", isSquaredBinarySearch(15))
print("isSquaredBinarySearch(16):", isSquaredBinarySearch(16))
print("isSquaredBinarySearch(17):", isSquaredBinarySearch(17))
print("isSquaredBinarySearch(18):", isSquaredBinarySearch(18))
print("isSquaredBinarySearch(19):", isSquaredBinarySearch(19))
print("isSquaredBinarySearch(20):", isSquaredBinarySearch(20))
print("isSquaredBinarySearch(21):", isSquaredBinarySearch(21))