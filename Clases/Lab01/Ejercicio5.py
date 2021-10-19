def borde(num):
  print(("*"*(num+1)) +"*"*len(cadena)+("*"*(num+1)))

def entreLineas(num):
  for i in range(0,num):
    print("*"+ (" "*num) + (" "*len(cadena))+ (" "*num) + "*")

def centro(num, cadena):
  print("*"+" "*num + cadena + " "*num+"*")


num = 1
if(num <= 0):
  print("Solo numeros positivos")
  quit()

cadena = input("String:")


borde(num)
entreLineas(num)
centro(num, cadena)
entreLineas(num)
borde(num)

