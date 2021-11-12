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
def dfs_recursive(matrix, startX, startY, simbVisited, simbPared):
    ## Visitar el primer valor
    matrix[startX][startY] = simbVisited
    print("marcando el punto (" + str(startX)+","+str(startY)+")")
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    
   
    for i in range(4):
        nx = dx[i] + startX
        ny = dy[i] + startY
        
        if(matrix[nx][ny] != simbVisited and matrix[nx][ny] != simbPared):
            dfs_recursive(matrix, nx, ny, simbVisited, simbPared)
        
    return matrix


## Generate matrix 5 of 5 with 
matri = [
    ["#","#","#","#","#","#"],
    ["#"," "," "," "," ","#"],
    ["#"," "," "," "," ","#"],
    ["#"," "," "," "," ","#"],
    ["#"," "," "," ","#"," "],
    ["#","#","#","#"," "," "],
]



print(dfs_recursive(matri, 2,2,"o", "#"))