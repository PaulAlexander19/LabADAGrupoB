# Ejercicio 04
import time
import matplotlib.pyplot as plt

# Algoritmo
def insertionSort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j = j - 1
        nums[j+1] = key
    return nums

# Retorna lo que tardo el algoritmo
def getTimeInsertionSort(numbers):
    tic = time.perf_counter()
    insertionSort(numbers)
    toc = time.perf_counter()
    return (toc - tic)



def createGraph(max):
    numbers = list(range(max+1,0,-1)) # Solo creamos una lista, para todos los casos
    x = []  # datos para el grafico, en el eje x
    y = []  # Datos para el grafico en el eje Y
    for i in range(0,max + 1,int(max/300)): # recorremos con que datos trabajaremos
        x.append(i)
        y.append(round(getTimeInsertionSort(numbers[0:i + 1]),4))

    print(x)    # depurar
    print(y)    # depurar

    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.plot(x, y)  # Plot some data on the axes.
    plt.show()


createGraph(1000) # recomendacion
