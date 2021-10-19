num1 = int(input("num1: "))
num2 = int(input("num2: "))
num3 = int(input("num3: "))

arr = [num1, num2, num3]

def selectionSort(aList):
    for i in range(len(aList)):
        least = i
        for k in range(i+1, len(aList)):
            if aList[k] < aList[least]:
                least = k

        swap(aList, least, i)

def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp

selectionSort(arr)

print(arr)
