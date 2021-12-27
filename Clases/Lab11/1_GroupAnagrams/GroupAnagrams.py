 
 # @Autor: Luque Ccosi, Paul Alexander
 # @Ejercicio: GroupAnagrams
 # Lab 11
 # @Descripcion: Dada una matriz de cadenas de cadenas, agrupe los anagramas. Puede devolver la respuesta en cualquier orden. Un anagrama es una palabra o frase formada reordenando las letras de una palabra o frase diferente, normalmente usando todas las letras originales exactamente una vez.

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}                        # copntiene los anagramas
        answer = []                         # respuesta

        for word in strs:                   # recorre la cadena
            string = "".join(sorted(word))  # ordenamos
            if string not in hashmap:                      
                hashmap[string] = [word]    # agerga la palabra y la conigura como [palabra]
            else:                           # esta en el hash               
                hashmap[string] += [word]   # agrega la palabra

        for key, value in hashmap.items():  # recorre el hash            
            answer.append(value)            # agregamosa a la matriz de respuesta
        return answer                       

# CASO DE PRUEBA
list = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(list))
list = [""]
print(Solution().groupAnagrams(list))
list = ["a"]
print(Solution().groupAnagrams(list))

