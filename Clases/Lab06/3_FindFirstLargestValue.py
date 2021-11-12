## 2 Encontrar el primer valor mayor o igual a x
## Autor: Luque Ccosi Paul Alexander

def findFirstLargestValue(number, numbers):
    ## es lo mismo que la busqueda binaria, pero ahora buscamos si es su raiz
    L = 0
    R = len(numbers) - 1
    value = (L + R) // 2

    while L <= R:
            
        mid = (L + R) // 2
        value = mid
        
        if(numbers[value] < number):
            if(numbers[value+1]>=number):
                return numbers[value+1]
            
        if numbers[mid] == number:
            return numbers[mid]
        elif numbers[mid] < number :
            L = mid + 1
        else:
            R = mid - 1
    return numbers[mid+1]

## casos de prueba para findFirstLargestValue


print("\nCaso de prueba:")
print("findFirstLargestValue(3, [1,2,3,4,5,6,7,8,9])")
print("Resultado esperado: 3")
print("Resultado obtenido:", findFirstLargestValue(3, [1,2,3,4,5,6,7,8,9]))

print("\nCaso de prueba:")
print("findFirstLargestValue(5, [1,2,3,4,5,6,7,8,9])")
print("Resultado esperado: 5")
print("Resultado obtenido:", findFirstLargestValue(5, [1,2,3,4,5,6,7,8,9]))

print("\nCaso de prueba:")
print("findFirstLargestValue(1, [1,2,3,4,5,6,7,8,9])")
print("Resultado esperado: 1")
print("Resultado obtenido:", findFirstLargestValue(1, [1,2,3,4,5,6,7,8,9]))

print("\nCaso de prueba:")
print("findFirstLargestValue(9, [1,2,3,4,5,6,7,8,9])")
print("Resultado esperado: 9")
print("Resultado obtenido:", findFirstLargestValue(9, [1,2,3,4,5,6,7,8,9]))

print("\nCaso de prueba:")
print("findFirstLargestValue(10, [1,2,3,4,5,6,7,8,11])")
print("Resultado esperado: 11")
print("Resultado obtenido:", findFirstLargestValue(10, [1,2,3,4,5,6,7,8,11]))

print("\nCaso de prueba:")
print("findFirstLargestValue(4, [1,2,3,5,6,8,10,12])")
print("Resultado esperado: 5")
print("Resultado obtenido:", findFirstLargestValue(4, [1,2,3,5,6,8,10,12]))

print("\nCaso de prueba:")
print("findFirstLargestValue(9, [1,2,3,5,6,8,10,12])")
print("Resultado esperado: 10")
print("Resultado obtenido:", findFirstLargestValue(9, [1,2,3,5,6,8,10,12]))