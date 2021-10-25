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
                return True
    return False