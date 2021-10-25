## Algoritmo ariginal

def greatestNumberN2(array):
    for i in array:
        isValTheGreatest = True
        for j in array:
            if i < j:
                isValTheGreatest = False
        if isValTheGreatest:
            return i

## Algoritmo convertido a N

def greatestNumberN(array):
    max = array[0]
    for i in array:
        if i > max:
            max = i
    return max
