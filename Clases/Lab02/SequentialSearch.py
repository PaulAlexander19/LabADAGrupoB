# Ejercicio 02

def sequentialSearch(list, n):
    num_found = False
    for i in list:
        if i == n:
            num_found = True
            break
    return num_found
    
nums = [12,2,43,1,2,4,23]   # Lista de datos
n = int(input(""))          # Numero a buscar


print(sequentialSearch(nums,n))

 