# Ejercicio 5. What is the time complexity in terms of O()?
# Autor: Luque Ccosi Paul Alexander

# O(log_2(n))
# resumes is an array

# Algoritmo:
def pick_resume(resumes):
    eliminate = "top"

    while len(resumes) > 1:
        if eliminate == "top":
            a = round(len(resumes) / 2)
            b =   len(resumes) 
            resumes = resumes[a:b]
            eliminate = "bottom"
        elif eliminate == "bottom":
            b = round(len(resumes) / 2)
            resumes = resumes[0:b]
            eliminate = "top"
    return resumes[0]

# Casos de prueba
resumes = "0123456789"
resumes2 = "holaMundo"

print("pick_resume de 0123456789 es: " + pick_resume(resumes))
print("pick_resume de holaMundo es: " + pick_resume(resumes2))

## *** ANALISIS DE LA COMPLEJIDAD ** ##

# La complejidad es O(log_2(n)) ya que recorre el bucle y en la siguinete iteración
# el tamaño se reduce a la mitad y en la siguiente tambien se reduce a la mitad
# y según lo que demostramos en los ejercicios anteriores, el resultado es un log(n)

