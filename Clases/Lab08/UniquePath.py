## UniquuOAth.py

def uniquePathsWithObstacles(self, obstacleGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    ## Creamos la estrcutura que nos ayudara
    caminos = [ [ 0 for y in range( len(obstacleGrid) ) ] for x in range( len(obstacleGrid[0]) ) ]
    
    for j in range(len(obstacleGrid)):
        for i in range(len(obstacleGrid[j])):
            
                if (i-1 < 0 and j-1 < 0):
                    caminos[i][j] = 1
                    continue
                ## lateral izquierdo
                elif (i-1 < 0):
                    if(obstacleGrid[i][j-1] != 1):
                        # caminos[i][j] = caminos[i-1][j]
                        caminos[i][j] = caminos[i][j-1]
                    else:
                        caminos[i][j] = 0
                ## Superior
                elif(j-1 < 0):
                    if(obstacleGrid[i-1][j] != 1):
                        caminos[i][j] = caminos[i-1][j]
                    else:
                        caminos[i][j] = 0
                else:
                    ## casos posibles 
                    if(obstacleGrid[i-1][j] == 1 ):
                        caminos[i][j] = caminos[i][j-1]
                    elif(obstacleGrid[i][j-1] == 1):
                        caminos[i][j] = caminos[i-1][j]
                    elif(obstacleGrid[i-1][j] == 1 and obstacleGrid[i][j-1] == 1):
                        caminos[i][j] = 0
                    else:
                        caminos[i][j] = caminos[i-1][j] + caminos[i][j-1]
    return caminos
                        
a = uniquePathsWithObstacles(None, [[0,0,0],[0,1,0],[0,0,0]])
print(a)