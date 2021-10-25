## Hallar la complejidad del algoritmod

## Algoritmo origianal escrito en javascript
function twoSum(array){
    for (let i = 0; i < array.length; i++) {
        for (let j = 0; j < array.length; j++) {
            if (i !== j && array[i] + array[j] === 10) {
                return true;
            }
        }
    }

    return false;
}

