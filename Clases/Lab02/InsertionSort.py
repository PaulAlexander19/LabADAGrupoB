# Ejercicio 03

def insertionSort(nums):
    for i in range(1, len(nums)):
        key = nums[i]       ## numero que ordenaremos
        j = i - 1       #Recorremos a la posicion anterior

        while j >= 0 and nums[j] > key:     # recorremos hacia atras, verificando que 'key' sea menor
            nums[j+1] = nums[j] ## recorremos
            j = j - 1
        nums[j+1] = key # recorremos
    
    return nums



numbers = [11,2,4,6,98,2,13,4,6]


insertionSort(numbers)
print(numbers)
