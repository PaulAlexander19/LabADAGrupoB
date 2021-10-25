## Hallar la complejidad del algoritmod

## Algoritmo origianal escrito en javascript
# function twoSum(array){
#     for (let i = 0; i < array.length; i++) {
#         for (let j = 0; j < array.length; j++) {
#             if (i !== j && array[i] + array[j] === 10) {
#                 return true;
#             }
#         }
#     }

#     return false;
# }


## Algoritmo en python

def twoSum(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j and array[i] + array[j] == 10:
                print(str(array[i]) +"-"+ str(array[j]))
                return True
    return False

# Probando algoritmo
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(twoSum(array))

# Analisis de complejidad del algoritmo
# Como el algoritmo tiene 2 ciclos for y en cada uno recorre el arreglo, la complejidad del algoritmo es O(n^2)