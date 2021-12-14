
import sys

## Creamos la clase grafo
class Graph():
    def __init__(self, vertices):
        self.V = vertices
        ## Matriz con pesos de aristas
        self.graoh = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    ## Metodo para imprimir el MST
    def printMST(self, parent):
        print("Egde \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    ## Imprime el valor total del MST
    def printValueMST(self, parent):
        total = 0
        for i in range(1, self.V):
            total += self.graph[i][parent[i]]
        print(total)
        
    ## Encuentra la minima arista que no esta en el conjunto y cree un bucle
    def minKey(self, key, mstSet):
        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return min_index

    ## Algoritmo para encontrar el MST
    def primMST(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V  
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1  

        for cout in range(self.V):

            u = self.minKey(key, mstSet)
            mstSet[u] = True

            for v in range(self.V):

                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)
        self.printValueMST(parent)


g = Graph(5)
g.graph = [ [0, 3, 0, 0, 7],
            [3, 0, 5, 2, 0],
            [0, 5, 0, 8, 0],
            [0, 2, 8, 0, 4],
            [7, 0, 0, 4, 0]]
 
g.primMST();