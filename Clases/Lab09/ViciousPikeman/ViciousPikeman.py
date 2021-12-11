## ViciousPikeman.py

## @Author: Paul Luque
## LABS: Lab09

def solveProblems(n, givenTime, timeSolve):

    # que tomaremos y la penalidad que recibiremos
    totalTime, penalty = 0, 0
    # Empezamos a iterar en la lista
    for i, t in enumerate(timeSolve):
        # Verificamos si es mayor al tiempo maximo
        if (totalTime + t) > givenTime:
            return i, penalty

        # agregamos el tiempo
        totalTime += t
        
        # Agregamos el tiempo que ha pasado hasta resolver
        # el ejercicio 
        
        penalty = (penalty + totalTime) % 1000000007
    return n, penalty

# Metodo principal del programa - Main

def main():
    # Recibimos los valores 
    n,t = map(int, input().split())
    # Recibimos los valores de A, B, C y T0
    a,b,c,t0 = map(int, input().split())
    # resolver cada ejercicio al Concursante
    timeSolve = [t0]

    # llenamos los tiempos de los demas
    for x in range(1, n):
        value = ((a * timeSolve[-1] + b) % c) + 1
        timeSolve.append(value)
    #  ordenar la lista
    timeSolve = sorted(timeSolve)
    print(*solveProblems(n, t, timeSolve))


main()