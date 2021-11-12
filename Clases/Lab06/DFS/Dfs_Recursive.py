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
    
    

## algoritmo como tal
def dfs_recursive(start):
    start.setVisited()
    print("marcando nodo" + str(start))
    for n in start.getNeighbors():
        if not n.isVisited():
            dfs_recursive(n)


## Casos de prueba

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

## generate a graph with nodes and edges
node1.addNeighbor(node2)
node1.addNeighbor(node3)
node1.addNeighbor(node4)
node2.addNeighbor(node4)
node2.addNeighbor(node5)
node3.addNeighbor(node6)
node3.addNeighbor(node7)

## Arbol 
              # 1
        #2              #5
    #4      5       #6    #7
    
print("Esperado: node1, node2, node3, node4, node5, node6, node7")   
dfs_recursive(node1)