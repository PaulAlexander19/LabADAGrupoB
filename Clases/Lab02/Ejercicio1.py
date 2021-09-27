## Ejercicio 01

n = int(input(":")) ## Numeros con los que se va a trabajar
k = int(input(":"))  ## Divisor
num_total = 0

for i in range(n):
    num = int(input("::")) ## Leemos los 'n' numeros
    if num % k == 0:
        num_total += 1


print(num_total)    