## Merge k Sorted Lists

## Luque Ccosi Paul Alexander

## Dada una lista ordenarnalas en una lista general, ordenadas por el orden de los numeros
## en otas palabras, ordenar en una cola de prioridad
import queue

def mergeList(lista):
    priority_queue = queue.PriorityQueue()
    res = []    ## aqui se almacenara 

    for i in lista:
        for j in i: ## recorremos todos los datos
            priority_queue.put(j) ## almacenamos en la lista de priridad

    while not priority_queue.empty():
        res.append(priority_queue.get()) ## agregamos en una lista el resultado

    return res

## Casos de prueba
print("[[1,4,5],[1,3,4],[2,6]]")
print(mergeList([[1,4,5],[1,3,4],[2,6]]))