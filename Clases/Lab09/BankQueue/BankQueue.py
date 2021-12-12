## TieRopes

## @Author: Paul Luque
## LABS: Lab09


import sys


def main():
    
    ## Recibimos los datos
    dataClientes = []
    def get_ints(): return map(int, sys.stdin.readline().strip().split())
    n, t = get_ints()
    n = int(n)
    t = int(t)
    tem = []
    for line in range(n):  # Por cada linea enviada al input iteraremos
        dinero, tiempo = get_ints()
        tem.append(dinero)
        tem.append(tiempo)
        dataClientes.append(tem)
        tem = []
    ## Ordenamos los datos
    dataClientes = sorted(dataClientes, key=lambda item :(item[0], t - item[1]), reverse=True)
    # print(dataClientes)
    print(solution(dataClientes, n, t))

def sorter(elem, max):
    a = max -  elem[1]
    return elem[0], max

def solution(dataCliente, numberPeople, totalTime):
    ## recibe una matriz , [0] dinero, [1] tiempo
    
    totalCash = 0
    
    waitingTime = 0
    
    select = [False]*totalTime
    
    
    while (waitingTime < numberPeople and not(len(dataCliente) == 0)):
        
        personActual = dataCliente[0]
        
        dataCliente.remove(dataCliente[0])
        
        start = personActual[1]
        
        while(start >= 0 and select[start]):
            start -= 1
    
        if(start != -1):
            waitingTime += 1
            select[start] = True
            totalCash += personActual[0]
            
    return totalCash
    
if __name__ == "__main__":
    main()