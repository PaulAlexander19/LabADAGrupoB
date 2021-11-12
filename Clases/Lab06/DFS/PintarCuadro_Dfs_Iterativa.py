# Algoritmo de busqueda por profundidad iterativo para pintar una matris
# Autor: Luque Ccosi Paul Alexander


# Implementación de una pila en pyhton
# Creamos la clase Stack
class Stack:
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


# algoritmo como tal para pintar
def dfs_iterative(matrix, startX, startY, simbVisited, simbPared):
    
    ## Visitar el primer valor, verificamos si es pares, y si esta en los limites
    try:
        if(matrix[startX][startY] != simbPared):
            matrix[startX][startY] = simbVisited
        else:
            print("es pared, no se pude pintar")
            return matrix
    except:
        print("Fuera del os limites")
        return matrix

    ## Insertando y marcando el punto
    S = Stack()
    print("Insertando (" + str(startX)+", "+str(startY)+")")
    punto = [startX, startY]
    print(punto)
    S.push(punto)
    print("Visitando nodo (" + str(startX)+", "+str(startY)+")")
    matrix[startY][startY] = simbVisited

    ## Verificamos si la lista esta vacia
    while not S.is_empty():
        v = S.pop()
        print("Eliminando (" + str(v[0])+", "+str(v[1])+")")

        ## Recorremos los puntos adyacentes
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        ## Recorremos los puntos adyacentes
        for i in range(4):
            nx = dx[i] + v[0]
            ny = dy[i] + v[1]

            # verificamos si esta dentro de los limites
            if((nx >= 0 and nx < len(matrix)) and (ny > 0 and ny < len(matrix[startX]))):

                # Verificamos si ya esta visitado o si es parte de la pared
                if(matrix[nx][ny] != simbVisited and matrix[nx][ny] != simbPared):

                    print("Visitando nodo (" + str(nx)+", "+str(ny)+")")
                    ## Marcamos el nodo visitado
                    matrix[nx][ny] = simbVisited
                    print("Insertando (" + str(nx)+", "+str(ny)+")")
                    ## Agregamos a la pila
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
printMatrix(dfs_iterative(matri, 1, 1, "o", "#"))  # despues
