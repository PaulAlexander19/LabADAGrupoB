n = int(input("n: "))
numbers = []
for i in range(n):
  num = int(input("num "+str(i+1)+": "))
  numbers.append(num)

for j in range(1, len(numbers)+1,1):
  print(numbers[-j])

