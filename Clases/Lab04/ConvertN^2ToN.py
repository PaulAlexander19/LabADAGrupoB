## Algoritmo ariginal

def greatestNumberN2(array):
    for i in array:
        isValTheGreatest = True
        for j in array:
            if i < j:
                isValTheGreatest = False
        if isValTheGreatest:
            return i




