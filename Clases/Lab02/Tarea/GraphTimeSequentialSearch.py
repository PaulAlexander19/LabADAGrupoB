# Ejercicio 04
import time
import matplotlib.pyplot as plt

# algoritmo
def sequentialSearch(list, n):
    num_found = False
    for i in list:
        if i == n:
            num_found = True
            break
    return num_found
    

# Obtenemos el tiempo
def getTimeSequentialSearch(numbers, num):
    tic = time.perf_counter()
    sequentialSearch(numbers, num)
    toc = time.perf_counter()
    return (toc - tic)



def createGraph(max):
    numbers = list(range(0,max+1,1)) # Solo creamos una lista, para todos los casos
    x = []  # datos para el grafico, en el eje x
    y = []  # datos para el grafico, en el eje y
    for i in range(0,max + 1,int(max/100)): # recorremos con que datos trabajaremos
        x.append(i)
        y.append(round(getTimeSequentialSearch(numbers[0:i + 1], i),4))

    print(x)    # Depurar
    print(y)    # Depurar

    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.plot(x, y)  # Plot some data on the axes.
    plt.show()


createGraph(1000000)
