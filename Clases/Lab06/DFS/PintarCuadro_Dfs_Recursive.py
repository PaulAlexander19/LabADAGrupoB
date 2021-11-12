## Algoritmo de busqueda por profundidad recursivo
## Autor: Luque Ccosi Paul Alexander


    

## algoritmo como tal
def dfs_recursive(matrix, startX, startY, simbVisited, simbPared):
    ## Visitar el primer valor
    matrix[startX][startY] = simbVisited
    print("marcando el punto (" + str(startX)+","+str(startY)+")")
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    
   
    for i in range(4):      ## buscamos en sus 4 adyecentes
        nx = dx[i] + startX
        ny = dy[i] + startY
        
        if(matrix[nx][ny] != simbVisited and matrix[nx][ny] != simbPared):  ## Verificamos si ya esta visitado o si es parte de la pared
            dfs_recursive(matrix, nx, ny, simbVisited, simbPared)
        
    return matrix


## Generate matrix 5 of 5 with 
matri = [
    ["#","#","#","#","#","#"],
    ["#","-","-","-","-","#"],
    ["#","-","-","-","-","#"],
    ["#","-","-","-","-","#"],
    ["#","-","-","-","#","-"],
    ["#","#","#","#","-","-"],
]



# Metodo para imprimir la matriz
def printMatrix(matrix):
    for i in matrix:
        for j in i:
            print(" " , j , end=" ")
        print()
        
        
printMatrix(matri)      ## antes
printMatrix(dfs_recursive(matri, 5,5,"o", "#"))  ## despues