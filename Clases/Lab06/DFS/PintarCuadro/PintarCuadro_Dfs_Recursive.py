## Algoritmo de busqueda por profundidad recursivo para pintar una matris
## Autor: Luque Ccosi Paul Alexander

## algoritmo como tal
def dfs_recursive(matrix, startX, startY, simbVisited, simbPared):
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

    ## Indicamos que Marcamos el punto, y hallamos los puntos adyacentes     
    print("marcando el punto (" + str(startX)+","+str(startY)+")")
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    
    ## Recorremos los puntos adyacentes
    for i in range(4):      
        nx = dx[i] + startX
        ny = dy[i] + startY
        
        ## ## verificamos si esta dentro de los limites
        if((nx >= 0 and nx < len(matrix)) and (ny > 0 and ny < len(matrix[startX]))):       
            
            ## Verificamos si ya esta visitado o si es parte de la pared
            if(matrix[nx][ny] != simbVisited and matrix[nx][ny] != simbPared):  
                dfs_recursive(matrix, nx, ny, simbVisited, simbPared)
            
    return matrix


# Metodo para imprimir la matriz
def printMatrix(matrix):
    for i in matrix:
        for j in i:
            print(" " , j , end=" ")
        print()

### DATOS DE PRUEBA
## Generate matrix 5 of 5 with 
matri = [
    ["#","#","#","#","#","#"],
    ["#","-","-","-","-","#"],
    ["#","-","-","-","-","#"],
    ["#","-","-","-","-","#"],
    ["#","-","-","-","#","-"],
    ["#","#","#","#","-","-"],
]


        
        
printMatrix(matri)      ## antes
printMatrix(dfs_recursive(matri, 2,2,"o", "#"))  ## despues