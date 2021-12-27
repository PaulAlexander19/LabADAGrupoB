 
 # @Autor: Luque Ccosi, Paul Alexander
 # @Ejercicio: StringMatching
 # Lab 11


import sys

def construct_partial_match_table(patron):
    
    string_length = len(patron)            
    current_prefix_length = 0                                       

    partial_match_table = [0] * string_length

    if string_length == 1:
        return partial_match_table

    # Repita cada carácter del patrón para comprobar los sufijos parciales en diferentes puntos del patrón.
    # Comenzamos en el índice 1 porque en el índice 0, trivialmente no hay un sufijo parcial posible
    for current_index, current_char in enumerate(patron[1:], 1):
        while current_prefix_length > 0 and patron[current_prefix_length] != current_char:
            current_prefix_length = partial_match_table[current_prefix_length - 1]

        if patron[current_prefix_length] == current_char:
            current_prefix_length += 1
        partial_match_table[current_index] = current_prefix_length
    return partial_match_table


# El algoritmo de Knuth-Morris-Pratt 
def kmp_string_search(given_string, patron):
    # Cree una tabla de coincidencias parciales para usar en el algoritmo de búsqueda KMP
    table = construct_partial_match_table(patron)
    given_string_length = len(given_string)
    patron_length = len(patron)

    index_to_begin_search = 0
    given_index = 0
    patron_index = 0
    locations_of_matches = []

    # Iterar a través de cada carácter de la cadena que deseamos comprobar.
    while given_string_length - index_to_begin_search > patron_length:
        while patron_index < patron_length and given_string[given_index] == patron[patron_index]:
            given_index += 1
            patron_index += 1

        # patron_index solo se incrementa mientras
        # substring[0:patron_index] == given_string[index_to_begin_search:given_index]
        # Entonces, si patron_index alcanza la longitud de la subcadena, sabemos que hemos encontrado una coincidencia para toda la subcadena
        if patron_index >= patron_length:
            locations_of_matches.append(str(index_to_begin_search))

        # Verificamos el valor en nuestra tabla de coincidencia parcial para la coincidencia más reciente que hemos encontrado.
        # Si esta coincidencia está en cualquier lugar más allá del comienzo de nuestra cadena, given_index permanece igual,
        # patron_index toma este valor, e index_to_begin_search intuitivamente se convierte en la diferencia en estos números
        if patron_index > 0 and table[patron_index - 1] > 0:
            index_to_begin_search = given_index - table[patron_index - 1]
            patron_index = table[patron_index - 1]

      
        else:
            if given_index == index_to_begin_search:
                given_index += 1
            index_to_begin_search = given_index
            if patron_index > 0:
                patron_index = table[patron_index - 1]

    # Nuestro código solo reconoce 'finding' una coincidencia de subcadena cuando incrementamos patron_index más allá de la longitud del
    # subcadena, y esto no puede suceder una vez que llegamos al final de nuestra cadena dada
    # Para dar cuenta de esto, simplemente verificamos por separado si el final de nuestra cadena dada coincide con nuestra subcadena
    if given_string[-patron_length:] == patron:
        locations_of_matches.append(str(len(given_string) - patron_length))
    print(' '.join(locations_of_matches))

# CASO DE PRUEBA
# Inicialice todas las variables booleanas y de cadena que usaremos durante nuestra prueba
string_to_check = ''
patron_to_check = ''
check_ready = False

# Leer cada línea independientemente del stdin
# En las líneas impares, se nos da el patrón para verificar
# En las líneas pares, se nos da la cadena para verificar
for line in sys.stdin:
    if not check_ready:
        patron_to_check = line.rstrip('\n')
        check_ready = True
    else:
        string_to_check = line.rstrip('\n')
        check_ready = False
        kmp_string_search(string_to_check, patron_to_check)