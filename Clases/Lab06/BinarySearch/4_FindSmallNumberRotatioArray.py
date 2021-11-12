## Encontrar el minimo en un arreglo rotado
## Autor: Luque Ccosi Paul Alexander

def findFirstLargestValue( numbers):
    L = 0
    R = len(numbers) - 1
    mid = (L + R) // 2      ## Division entera
    answer = 0              ## Posicion del minimo

    while L <= R:           ## Mientras no se cruce los limites
            
        mid = (L + R) // 2      
        
        if(numbers[L] < numbers[mid]):      ## Si el minimo esta en la mitad izquierda
            answer =numbers[L]          ## Se asigna el minimo
            L = mid             ## Se cambia el limite izquierdo
        
        elif numbers[mid] < answer :        ## Si el minimo esta en la mitad derecha
            answer = numbers[mid]
            R = mid
        else:       
            L = L + 1
    return answer

## casos de prueba para findFirstLargestValue


print("\nCaso de prueba:")
print("findFirstLargestValue([6,8,10,12,1,2,3,5])")
print("Resultado esperado: 1")
print("Resultado obtenido:",findFirstLargestValue([6,8,10,12,1,2,3,5]))