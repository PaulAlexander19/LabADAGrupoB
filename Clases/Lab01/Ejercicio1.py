from functools import reduce

n = int(input("n: "))
numbers = []
for i in range(n):
  num = int(input("num "+str(i+1)+": "))
  numbers.append(num)

suma = reduce(lambda x, y: x + y, numbers)

print(suma)
