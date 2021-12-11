## MaxNonoverlappingSegments

## @Author: Paul Luque
## LABS: Lab09


## Para hallar la solucion tenemos que ver en cada paso cual nos combiene, tenemos que iterar todos
## Los elementos
def solution(A,B):
    n = len(A)
    ## Verificamos si hay un elemento
    if n <= 1:
        return n

    ## Inicializamos el contador
    count = 1
    ## Este valor nos ayudara a saber si nos combiene o no
    prev = B[0]
    
    ## Iteramos todos los elementos
    for i in range(1, n):
        ## Verificamos si nos conviene
        if A[i] > prev:
            ## Incremenamos el contador
            count += 1
            prev = B[i]
            
    return count

## Casos de prueba ##

a = [1,3,7,9,9]
b = [5,6,8,9,10]

# use solution with a and b as parameters
print(solution(a,b))