# WateringGrass.py

# @Author: Paul Luque
## LABS: Lab09


import sys
from math import sqrt


def solution(aspersores, l, n):
    useAmount, currentSprinkler, currentLen = 0, 0, 0
    # Iteraremos hasta que toda el cesped este regado
    while True:
        # La posicion mas lejana al iniciar nuestro regado seria de -1.
        masAlejado = -1
        # Iteraremos mientras haya aspersores y la longitud del
        # aspersor actual no sea mayor a la longitud regada por otros aspersores

        while currentSprinkler < n and aspersores[currentSprinkler][0] <= currentLen:
            masAlejado = max(masAlejado, aspersores[currentSprinkler][1])
            currentSprinkler += 1

        # En caso que no se haya podido seleccionar ningun aspersor que
        # riege correctamente devolveremos un -1
        if masAlejado == -1:
            return -1

        useAmount += 1
        currentLen = masAlejado
        if currentLen >= l:

            return useAmount


def main():
    lines = 0  # contador de lineas en 0
    w = 0
    for line in sys.stdin:  # Por cada linea enviada al input iteraremos
        if lines == 0:
            n, l, w = map(int, line.split())
            aspersores = []
            lines = n
        else:
            lines -= 1  # Se reduce en una unidad cada vez que registremos los datos de un aspersor
            h, r = map(int, line.split())
            if (2 * r) > w:
                # distancia de rango de riego
                d = sqrt((r ** 2) - ((w / 2) ** 2))
                # Agregamos su area de riego a la lista de aspersores
                aspersores.append((h - d, h + d))
            if lines == 0:  # Se ordena
                aspersores = sorted(aspersores)

                print(solution(aspersores, l, len(aspersores)))


main()
