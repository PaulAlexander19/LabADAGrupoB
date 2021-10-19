valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = list(filter(lambda x : x % 2 == 0, valores))
impares = list(filter(lambda x : x % 2 != 0, valores))

print(pares)
print(impares)

