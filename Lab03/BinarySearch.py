
def BinarySearch(numbers, n):
    numElements = len(numbers)
    if(numElements == 1):
        return (n == numbers[0])
    
    mitad = numElements // 2
    if(numbers[mitad] == n):
        return True
    elif (n < numbers[mitad]):
        return BinarySearch(numbers[0:mitad],n)        
    else:
        return BinarySearch(numbers[mitad:len(numbers)],n)

lista = [1,3,5,7,9]

print(BinarySearch(lista, 30))