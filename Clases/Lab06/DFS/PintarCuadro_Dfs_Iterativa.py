# Algoritmo de busqueda por profundidad iterativo
# Autor: Luque Ccosi Paul Alexander


# Implementación de una pila en pyhton

from typing import List


class Stack:  # Creamos la clase Stack
    def __init__(self):
        self.items = []

    def is_empty(self):  # Metodo para verificar si la pila esta vacia
        return self.items == []

    def push(self, item):  # Metodo para insertar elementos a la pila
        self.items.insert(0, item)

    def pop(self):  # Metodo para eliminar el ultimo elemento apilado
        return self.items.pop(0)

    def print_stack(self):  # Metodo para mostrar los elementos de la pila
        print(self.items)


class Pount():
    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def __str__(self):
        return "("+str(self.x)+", "+str(self.y)+")"


# algoritmo como tal
def dfs_iterative(matrix, startX, startY, simbVisited, simbPared):
    S = Stack()
    print("Insertando (" + str(startX)+", "+str(startY)+")")
    punto = [startX, startY]
    print(punto)
    S.push(punto)
    print("Visitando nodo (" + str(startX)+", "+str(startY)+")")
    matrix[startY][startY] = simbVisited

    while not S.is_empty():
        v = S.pop()
        print("Eliminando (" + str(v[0])+", "+str(v[1])+")")

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        for i in range(4):
            nx = dx[i] + v[0]
            ny = dy[i] + v[1]

            # verificamos si esta dentro de los limites
            if((nx >= 0 and nx < len(matrix)) and (ny > 0 and ny < len(matrix[startX]))):

                # Verificamos si ya esta visitado o si es parte de la pared
                if(matrix[nx][ny] != simbVisited and matrix[nx][ny] != simbPared):

                    print("Visitando nodo (" + str(nx)+", "+str(ny)+")")
                    matrix[nx][ny] = simbVisited
                    print("Insertando (" + str(nx)+", "+str(ny)+")")
                    tempo = [nx, ny]
                    S.push(tempo)
    return matrix

# Metodo para imprimir la matriz


def printMatrix(matrix):
    for i in matrix:
        for j in i:
            print(" ", j, end=" ")
        print()


# DATOS DE PRUEBA
# Generate matrix 5 of 5 with
matri = [
    ["#", "#", "#", "#", "#", "#"],
    ["#", "-", "-", "-", "-", "#"],
    ["#", "-", "-", "-", "-", "#"],
    ["#", "-", "-", "-", "-", "#"],
    ["#", "-", "-", "-", "#", "-"],
    ["#", "#", "#", "#", "-", "-"],
]


printMatrix(matri)  # antes
printMatrix(dfs_iterative(matri, 5, 5, "o", "#"))  # despues
