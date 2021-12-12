# def sorter(elem, max):
#     a = max -  elem[1]
#     # b = elem[1]
#     return elem[0], max


# data = [[1000, 1], [2000, 2],[2000, 0], [500, 2], [1200, 0],[500,0]]

# max = 1000
# data = sorted(data, key=lambda item :(item[0], max - item[1]), reverse=True)
# print(data)


import sys


def main():
    
    ## Recibimos los datos
    flag = True
    dataClientes = []
    for line in sys.stdin:  # Por cada linea enviada al input iteraremos
        if flag:
            n, t = map(int, line.split())
            tem = []
            flag = False
        else:
            dinero, tiempo = map(int, line.split())
            tem.append(dinero)
            tem.append(tiempo)
            dataClientes.append(tem)
            tem = []
    ## Ordenamos los datos
    dataClientes = sorted(dataClientes, key=lambda item :(item[0], t - item[1]), reverse=True)
    print(dataClientes)
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
    

main()