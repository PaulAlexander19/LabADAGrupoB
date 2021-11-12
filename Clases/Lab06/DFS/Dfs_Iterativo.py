## Algoritmo de busqueda por profundidad iterativo
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
   
   
# Implementación de una pila en pyhton

class Stack: # Creamos la clase Stack
    def __init__(self):
        self.items = []
    
    def is_empty(self): # Metodo para verificar si la pila esta vacia
        return self.items == []
    
    def push(self, item): # Metodo para insertar elementos a la pila
        self.items.insert(0, item)
    
    def pop(self): # Metodo para eliminar el ultimo elemento apilado
        return self.items.pop(0)
    
    def print_stack(self): # Metodo para mostrar los elementos de la pila
        print(self.items) 
    

## algoritmo como tal
def dfs_iterative(start):
    S = Stack()
    print("Insertando" + str(start))
    S.push(start)
    print("Visitando nodo "+str(start))
    start.setVisited();
    while not S.is_empty():
        v = S.pop()
        print("Eliminando "+str(v))
        for w in v.getNeighbors():
            if not w.isVisited():
                print("Visitando nodo "+str(w))
                w.setVisited()
                print("Insertando" + str(w))
                S.push(w)
                

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
node2.addNeighbor(node3)
node2.addNeighbor(node5)
node3.addNeighbor(node6)
node3.addNeighbor(node7)
node5.addNeighbor(node6)


## Arbol 
              # 1
        #2              #5
    #4      5       #6    #7
    
print("Esperado: node1, node2, node3, node4, node5, node6, node7")   
dfs_iterative(node1)