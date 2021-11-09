# Ejercicio: 4. What is the time complexity in terms of O()?
# Autor: Luque Ccosi Paul Alexander


#  O(n * m)
# n :
# m :
#"fgh" "abcdefghi"


# Algoritmo en python
def findNeedle(needle, haystack):
    needle_index = 0
    haystack_index = 0
    found_needle = False

    while haystack_index < len(haystack):
        if needle[needle_index] == haystack[haystack_index]:
            found_needle = True
            while needle_index < len(needle):
                if needle[needle_index] != haystack[haystack_index + needle_index]:
                    found_needle = False
                    break
                needle_index += 1

            if found_needle:
                return True
            needle_index = 0

        haystack_index += 1
    return False

# Ejemplos 
cadenaA = "abcdefghi"
cadenaB = "bac"

print(findNeedle(cadenaB, cadenaA))


## *** ANALISIS DE LA COMPLEJIDAD ** ##

# La complejida es O(n*m) ya que en el bucle interior recorre "needle" y en el bucle exterior recorre"haystack"
# por lo que la complejidad es la multiplicacion de los tamaños de las 2 entradas.
