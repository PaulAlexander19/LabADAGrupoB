# @Autor: Luque Ccosi, Paul Alexander
# @Ejercicio: SpellingBee
# Lab 11
# DESCRIPCION: The New York Times publica un acertijo diario llamado "Spelling Bee". En este rompecabezas, se muestran 7 letras en una disposición hexagonal de 6 letras alrededor de una letra central. La tarea es encontrar tantas palabras como sea posible que contienen solo letras que se muestran en el hexágono, tienen al menos una longitud de 4, y contienen la letra central. Una letra puede usarse más de una vez y no es necesario usar todas las letras. Encuentre todas las soluciones a un acertijo del concurso de ortografía en su diccionario.


def isMatchingWord(word, hexagonLetters):
    # recibe una palabra y las letras en disposicion hexadecimal, retorna un booleano si la palabra es coincidente con hexagonLetters
    for letter in word:
        if letter not in hexagonLetters:
            return False
    return True


# entrada de las letras en disposicion hexadecimal
hexagonLetters = input()
# Primera letra hexagonal
mandatoryFirstHexagonletter = hexagonLetters[0]

# número de palabras del diccionario
numberOfDictionaryWords = int(input())

for _ in range(numberOfDictionaryWords):
    # ingreso de palabras
    dictionaryWord = input()
    if len(dictionaryWord) < 4:                             # si la longitud es menor a 4
        continue

    # si la primera letra hexagonal no esta en el diccionario de palabras
    if mandatoryFirstHexagonletter not in dictionaryWord:
        continue

    if isMatchingWord(dictionaryWord, hexagonLetters):      
        # Si es concidente
        print(dictionaryWord)
