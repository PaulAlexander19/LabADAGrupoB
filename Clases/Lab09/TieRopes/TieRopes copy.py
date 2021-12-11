## TieRopes

## @Author: Paul Luque
## LABS: Lab09


## Hallar el numero maximo de cuerdas mayores a K

def solution(K, A):
    # numeros de cuerdas finales
    countRopes = 0
    
    # variable para apoyarnos, tamaño temporal de una cuerda   
    rodeLenTem = 0
      
    for i in range(0, len(A)):
        
        # Agregamos la longitud de la cuerda actual  
        rodeLenTem += A[i]  
        
        # Si el tamanio es mayor o igual al valor de K
        if(rodeLenTem >= K):
            rodeLenTem = 0
            countRopes += 1
         
    return countRopes  


# Casos de Prueba

a = [1, 2, 3, 4, 1, 1, 3]

print(solution(4, a))
