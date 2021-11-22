## Encontrar el minimo en un arreglo rotado
## Autor: Luque Ccosi Paul Alexander

def findFirstLargestValue(array):
    L = 0                          
    R = len(array) - 1             
    min = array[0]                 
    while (L <= R):                # mientras el indice inferior sea menor al limite superior
        mid = L + (R - L) // 2     # calculamos el indice medio
        if min < array[mid]:       # verificamos si el limite inferior es menor al indice medio                     
            L = mid + 1            # EL LIMITE INFERIOR ES EL INDICE MEDIO + 1
        else:                      # Si el elemento en el limite inferior es menor al elemento en el indice medio
            if array[mid] < min:   
                min = array[mid]   # Asignamos a "min" el elemento del indice medio
                R = mid            
            else:
                L += 1             # incrmentamos el indice inferior
    return min                     

# CASO DE PRUEBA
    
array = [1, 3, 5, 7, 9, 11, 13, 18]
print(array)
print("Menor del array: ", findFirstLargestValue(array))
print(array)
array = [3, 5, 7, 9, 11, 13, 18, 1]
print("Menor del array: ", findFirstLargestValue(array))
print(array)
array = [5, 7, 9, 11, 13, 18, 1, 3]
print("Menor del array: ", findFirstLargestValue(array))
print(array)
array = [7, 9, 11, 13, 18,1, 3, 5]
print("Menor del array: ", findFirstLargestValue(array))
print(array)
array = [11, 13, 18, 1, 3, 5, 7, 9]
print("Menor del array: ", findFirstLargestValue(array))
print(array)
array = [13, 18, 1, 3, 5, 7, 9, 11]
print("Menor del array: ", findFirstLargestValue(array))
print(array)
array = [18, 1, 3, 5, 7, 9, 11, 13, ]
print("Menor del array: ", findFirstLargestValue(array))
