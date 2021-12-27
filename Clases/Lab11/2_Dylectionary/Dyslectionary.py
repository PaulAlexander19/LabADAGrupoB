 
 # @Autor: Luque Ccosi, Paul Alexander
 # @Ejercicio: Dyslectionary
 # Lab 11
 # @Descripcion: SE VA A RECIBIR 100 GRUPOS DE PALABRAS, ELLOS VAN ESTAR SEPARADOS POR SALTOS DE LINEA. ESTOS BLOQUES DE PROBLEMAS DEBEN SER ORDENADOS ALFABETICAMENTE DESDE ATRAS(EL FINAL) HACIA EL CARACTER DE ADELANTE, SE DEBE RETORNAR EL DICCIONARIO DE PALABRAS ORDDENADAS AL REVES.


def sortAndPrint(longest, words):
  
    for w in sorted(words, key = lambda w: w[::-1]): # ordenamos el bloque de las palabras con una funcion lambda       
        padding = ' ' * (longest - len(w))           # Se Crea Un Padding Con ' ' Para Que Se Justifique La Palabra (Longitud Mas Larga - Longitud Palabra En Iteracion)
       
        print(f'{padding}{w}')                       # Imprimimos

# MAIN
def main():
    # VARIABLES
    longest, words = -1, []                          # (LONGITUD, BLOQUE DE PALABRAS)
   
    while True:                                      
        try:                        
            word = input()                                  # Ingresamos la palabra
            if not word:                                    # si esta vacia o hay un salto de linea               
                sortAndPrint(longest, words)                # ordenamos               
                print()                                     
                longest, words = -1, []                     
            
            else:                                           # si no esta vacia
                longest = max(longest, len(word))           # elegimos la longitud máxima
                words.append(word)                          # agergamos al bloque de palabras
        
        except EOFError:                                    # por si falla

            sortAndPrint(longest, words)                    
            
            break                                           

if __name__ == "__main__":                                  
    main()                                                  