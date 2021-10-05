# Ejercicio 04
import time
import matplotlib.pyplot as plt

# Algoritmo
def binarySearch(numbers, n):
    numElements = len(numbers)
    if(numElements == 1):
        return (n == numbers[0])
    
    mitad = numElements // 2
    if(numbers[mitad] == n):
        return True
    elif (n < numbers[mitad]):
        return binarySearch(numbers[0:mitad],n)        
    else:
        return binarySearch(numbers[mitad:len(numbers)],n)

# Retorna lo que tardo el algoritmo
def getTimeBinarySearch(numbers, n):
    tic = time.perf_counter()
    binarySearch(numbers, n)
    toc = time.perf_counter()
    return (toc - tic)



def createGraph(max, sal):
    # numbers = list(range(max+1,0,-1)) # Solo creamos una lista, para todos los casos
    x = []  # datos para el grafico, en el eje x
    y = []  # Datos para el grafico en el eje Y
    
    for i in range(0,max,sal): # recorremos con que datos trabajaremos
        x.append(i+1)
        lista = list(range(0, (i+1)*2,2))
        time = round(getTimeBinarySearch(lista,3),4) # Siempre buscamos el numero 3
        y.append(time)

    print(x)    # depurar
    print(y)    # depurar

    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.plot(x, y)  # Plot some data on the axes.
    plt.show()



def main(numrArreglo=50000, numSalto=50):
    createGraph(numrArreglo, numSalto) # recomendacion

__main__  = main()