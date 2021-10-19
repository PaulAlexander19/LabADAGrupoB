num = int(input("n:"))
if(num <= 0):
  print("Solo numeros positivos")
  quit()

cadena = input("String:")

print(("*"*(num+1)) +"*"*len(cadena)+("*"*(num+1)))

for i in range(0,num):
  print("*"+ (" "*num) + (" "*len(cadena))+ (" "*num) + "*")

print("*"+" "*num+cadena+" "*num+"*")

for i in range(0,num):
  print("*"+ (" "*num) + (" "*len(cadena))+ (" "*num) + "*")

print(("*"*(num+1)) +"*"*len(cadena)+("*"*(num+1)))

