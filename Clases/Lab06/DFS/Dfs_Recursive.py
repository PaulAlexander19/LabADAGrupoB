## Algoritmo de busqueda por profundidad recursivo
## Autor: Luque Ccosi Paul Alexander


## Para que funcione correcamente nos apoyaremos de una clase adicional

class Node():
    def __init__(self, valueInitial):
        self.valueInitial = valueInitial
        self.visited = False
        self.neighbors = []
    
    def addNeighbor(self, node):
        self.neighbors.append(node)
    
    
    def getNeighbors(self):
        return self.neighbors
    
    def getValue(self):
        return self.valueInitial
    
    def setVisited(self):
        self.visited = True
    
    def isVisited(self):
        return self.visited
    
    def __str__(self):
        return str(self.valueInitial)
    
    

def dfs_recursive(graph, start):
    start.visited = True
    print("marcando nodo" + str(start))
    for n in start.getNeighbors():
        if not n.visited:
            dfs_recursive(graph, n)


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

## generate a graph with nodes and edges


node1.addNeighbor(node2)
node2.addNeighbor(node5)
node2.addNeighbor(node4)
node2.addNeighbor(node3)

dfs_recursive(node1, node1)