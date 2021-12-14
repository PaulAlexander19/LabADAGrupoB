
import sys

## Varible globales 
INFINITY = sys.maxsize

## Creamos la clase grafo
class Graph():
    def __init__(self, vertices):
        self.V = vertices
        ## Matriz con pesos de aristas
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        ## arreglo con el camino
        self.path = [None] * self.V  

    ## Metodo para imprimir el MST
    def printMST(self):
        print("Egde \tWeight")
        for i in range(1, self.V):
            print(self.path[i], "-", i, "\t", self.graph[i][self.path[i]])

    ## Imprime el valor total del MST
    def printValueMST(self):
        total = 0
        for i in range(1, self.V):
            total += self.graph[i][self.path[i]]
        print(total)
        
    ## Encuentra la minima arista que no esta en el conjunto y cree un bucle
    def minKey(self, key, nodeVisited):
        min = INFINITY

        for v in range(self.V):
            if key[v] < min and nodeVisited[v] == False:
                min = key[v]
                min_index = v
        ## Retorna el nodo al cual visitaremos
        return min_index

    ## Algoritmo para encontrar el MST
    def primMST(self):
        key = [INFINITY] * self.V
        key[0] = 0
        nodeVisited = [False] * self.V

        ## alcualizamos el camino, el inicio del camino
        self.path[0] = -1  

        for cout in range(self.V):

            u = self.minKey(key, nodeVisited)
            nodeVisited[u] = True ## Visitamos el nodo

            ## Recorremos solo los nodos, actualizando key y los caminos
            for v in range(self.V):

                ## actualizamos el key de los nodos adyacentes que no estes visitados , tmbien actualizamos el camino
                if self.graph[u][v] > 0 and nodeVisited[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    self.path[v] = u



g = Graph(5)
g.graph = [ [0, 3, 0, 0, 7],
            [3, 0, 5, 2, 0],
            [0, 5, 0, 8, 0],
            [0, 2, 8, 0, 4],
            [7, 0, 0, 4, 0]]
 
g.primMST();
g.printValueMST()
print(g.path)