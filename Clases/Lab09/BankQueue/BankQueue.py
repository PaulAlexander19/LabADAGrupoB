## BankQueue

## @Author: Paul Luque
## LABS: Lab09


import sys


def main():
    
    ## Metodo para recibir datos
    def get_ints(): return map(int, sys.stdin.readline().strip().split())
    
    ## MAtris donde estaran los datos de los clientes
    dataClientes = []
    ## Obtenemos los datos
    n, t = get_ints()
    n = int(n)
    t = int(t)
    
    ## Lista temporal para ingresar los datos del os clientes
    tem = []
    for line in range(n):  # Ingesamos los datos
        dinero, tiempo = get_ints()
        tem.append(dinero)
        tem.append(tiempo)
        ## Agregamos a la matriz
        dataClientes.append(tem)
        tem = []
        
    ## Ordenamos los datos por su dinero, luego por su tiempo ("t - item[1]") es para que ordener en de manera inversa eso 
    dataClientes = sorted(dataClientes, key=lambda item :(item[0], t - item[1]), reverse=True)
    print(solution(dataClientes, n, t))

## Metodo para ordenar 
def sorter(elem, max):
    a = max -  elem[1]
    return elem[0], max

## Metodo que soluciona el problema
def solution(dataCliente, numberPeople, totalTime):
    ## recibe una matriz , [0] dinero, [1] tiempo
    
    ## el dinemo total
    totalCash = 0
    
    ## TImepo de espera
    waitingTime = 0
    
    ## para ayudarnos con los tiempos ocupados
    select = [False]*totalTime
    
    ## iteramos mientras en tiempo sea menos a la cantidad 
    while (waitingTime < numberPeople and not(len(dataCliente) == 0)):
        
        ## Obtenemos la persona actual
        personActual = dataCliente[0]
        dataCliente.remove(dataCliente[0])
        
        ## Tiempo de inicio
        start = personActual[1]
        
        ## Verificamos si la posicion esta libre o no
        while(start >= 0 and select[start]):
            start -= 1
    
        ## no hay espacio
        if(start != -1):
            ## Establecemos el timepo de atencion para el cliente
            waitingTime += 1
            select[start] = True
            ## Recaudamos su dinero
            totalCash += personActual[0]
            
    return totalCash
    
if __name__ == "__main__":
    main()