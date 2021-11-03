## Review of Time Complexity ##

def ejercicio1(n):
    # Q1: What is the time complexity of
    i = 0
    while (i < n):
        i = +1

    # La complejidad temporal de este algoritmo es O(n) porque el bucle se ejecuta n veces.

        # A1: O(n)
        # for (i = 0; i < n; i++) {   // n + 1
        #     statement;               // n
        # }


# ----------------------------------------------------------------------------------------------


def ejercicio2(n):
    i = n
    while(i > 0):
        i = -1

    # la complejidad temporal de este algoritmo es O(n) porque el bucle se ejecuta n veces.

        # // A2: O(n)


# ----------------------------------------------------------------------------------------------


def ejercicio3(n):
    i = 0
    while(i < n):
        i = i + 5

    # la complejidad temporal de este algotimo es O(n/5) pero se pude trabajar con O(n).


# ----------------------------------------------------------------------------------------------


def ejercicio4(n):
    i = 0
    while(i < n):
        j = 0
        while(j < n):
            j = j+1
        i = i+1

    # La complejidad temporal de este algoritmo es O(n^2) porque el bucle se ejecuta n veces y dentro de cada bucle se ejecuta n veces.

        #     // A4: O(n^2)
        #     for (i = 0; i < n; i++) {       // n + 1
        #         for (j = 0; j < n; j++) {   // n * (n + 1)
        #             statement;              // n * n
        #             cout << "i" << '\n';
        #     }
        # }


# ----------------------------------------------------------------------------------------------


def ejercicio5(n):
    i = 0
    while(i < n):
        j = 0
        while(j < i):
            i = j + 1
        i = i + 1
    ## *** ANALISIS DE LA COMPLEJIDAD ** ##
    #  la complejidad del algoritmo es o(n^2) ya que el buble superior se ejecuta n veces
    #  pero el buble interior se ejecuta la cantidad de i veces en un punto llegara que i sera cerca a n y por lo tanto
    #  j recorrera n veces

        # // A5:
        # // Tracing the values of the variables
        # //  i   j      no of times
        # // ------------------------
        # //  0   0 ❌     0
        # // ------------------------
        # //  1   0 ✔️     1
        # //      1 ❌
        # // ------------------------
        # //  2   0 ✔️     2
        # //      1 ✔️
        # //      2 ❌
        # // ------------------------
        # //  .
        # //  .
        # //  .
        # // ------------------------
        # //  n             n

        # // 1 + 2 + 3 + ... + n = n * (n + 1) / 2
        # // O(n^2)


# ----------------------------------------------------------------------------------------------


def ejercicio6(n):
    p = 0
    i = 1
    while(p <= n):
        p = p + i
        i = i + 1

    ## *** ANALISIS DE LA COMPLEJIDAD ** ###
    # la complejidad es de O(n^(1/2)) ya que en cada iteración en P se almacena la suma de los primeros "i" numeros
    #  y esto se rompe cuando la suma pasa n

        # // A6:
        # //  i       p
        # // ------------------------
        # //  1       0 + 1 = 1
        # //  2       1 + 2
        # //  3       1 + 2 + 3
        # //  4       1 + 2 + 3 + 4
        # //  .
        # //  .
        # //  .
        # //  k       1 + 2 + 3 + 4 + ... + k

        # // Assume k > n
        # // p = k * (k + 1) / 2
        # //               p > n
        # // k * (k + 1) / 2 > n
        # // k^2 > n
        # // k > sqrt(n)
        # // O(n^(1/2))


# ----------------------------------------------------------------------------------------------


def ejercicio7(n):
    i = 1
    while(i < n):
        i = i * 2

    ## *** ANALISIS DE LA COMPLEJIDAD ** ##
    # El algoritmo tiene una complejidad de O(log_2(n)) ya que se ejecuta hasya
    # el paso 2^k entonces para que ya no se cumpla la condición es log_2(n)

        # // A7:
        # //  i
        # // ------------------------
        # //  1
        # //  1 * 2 = 2
        # //  2 * 2 = 2^2
        # //  2 * 2^2 = 2^3
        # //  .
        # //  .
        # //  .
        # //  2^k

        # // Assume i >= n
        # // Therefore i = 2^k
        # //      2^k >= n
        # //       2^k = n
        # //         k = log_2(n)
        # // O(log_2(n))


# ----------------------------------------------------------------------------------------------


def ejercicio8(n):
    i = n
    while(i >= 1):
        i = i/2

    ## *** ANALISIS DE LA COMPLEJIDAD ** ##
    # La complejidad es de log_2(n) ya que i tiene la forma (n/2^k)
    # y para que se rompa la condicion k tiene que ser log_2(n)

        # //  i
        # // ------------------------
        # //  n
        # //  n / 2
        # //  n / 2^2
        # //  n / 2^3
        # //  .
        # //  .
        # //  .
        # //  n / 2^k

        # // Assume that i < 1
        # // Therefore n / 2^k < 1
        # //           n / 2^k = 1
        # //                 n = 2^k
        # //                 k = log_2(n)
        # // A8: O(log_2(n))


# ----------------------------------------------------------------------------------------------


def ejercicio9(n):
    i = 0
    while(i*i < n):
        i = i + 1

    ## *** ANALISIS DE LA COMPLEJIDAD ** ##
    # Para que el ciclo termine, tenemos que asumir que i^2 = n por lo que la complejidad es O(sqrt(n))

        # // Condition       i * i < n
        # // To finish       i * i >= n
        # // We assume that     i^2 = n
        # //                      i = sqrt(n)
        # // A9: O(sqrt(n))


# ----------------------------------------------------------------------------------------------


def ejercicio10(n):
    i = 0
    while(i < n):
        i = i + 1

    j = 0
    while(j < n):
        j = j + 1

    ## *** ANALISIS DE LA COMPLEJIDAD ** ##
    # la complejidad es O(n) porque en cada ciclo e O(n) y en total seria 2 * n

        # // A10: O(n)
        # for (i = 0; i < n; i++) {
        #     statement;          // n
        # }

        # for (j = 0; j < n; j++) {
        #     statement;          // n
        # }
        #                         // 2 * n


# ----------------------------------------------------------------------------------------------


def ejercicio11(n):
    p = 0
    i = 1
    while(i < n):
        p = p + 1
        i = i * 2

    j = 1
    while(j < p):
        j = j * 2

    ## *** ANALISIS DE LA COMPLEJIDAD ** ##
    # La complejidad es log(log(n)) es un ejecto cadena, el primer buble ya lo resolvimos
    # y sale log(p) en el segundo bucle es la misma idea log(p), seria log(log(p))

        # // A11:
        # p = 0
        # // (2)
        # for (i = 1; i < n; i = i * 2) {
        #     p++;                    // p = log(n)
        # }

        # // (1)
        # for (j = 1; j < p; j = j * 2) {
        #     statement;              // log(p)
        # }

        # // So, we have log(p) and p = log(n)
        # // replacing log log(n)
        # // O(log log(n))


# ----------------------------------------------------------------------------------------------


def ejercicio12(n):
    i = 0
    while(i < n):
        j = 1
        while(j < n):
            j = j * 2
        i = i + 1

    ## *** ANALISIS DE LA COMPLEJIDAD ** ##
    # La complejidad es O(n*log(n)) por que el ciclo interno es O(log(n)) y el ciclo externo es O(n)
    # La complejidad es nlog(n) entonces O(nlog(n))

        # // (1) This repeats n times
        # // (2) and this inner loop n times * log(n)
        # // (3) and this statement n times * log(n)
        # // Adding them together n + 2 n * log(n)
        # // O(n log(n))


# ----------------------------------------------------------------------------------------------


# // Review
# for (i=0
#      i < n
#      i++) // O(n)


# for (i=0
#      i < n
#      i=i+2) // O(n)


# for (i=n
#      i >= 1
#      i--) // O(n)


# for (i=1
#      i < n
#      i=i*2) // O(log_2(n))


# for (i=1
#      i < n
#      i=i*3) // O(log_3(n))


# for (i=n
#      i >= 1
#      i=i/2) // O(log_2(n))


# Ejercicios adicionales### ---------------------------------------------------------------------


# 4. What is the time complexity in terms of O()?
# O(n * m)
# n :
# m :
"fgh" "abcdefghi"


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




## *** ANALISIS DE LA COMPLEJIDAD ** ##
# La complejida es O(n*m) ya que en el bucle interior recorre "needle" y en el bucle exterior recorre"haystack"
# por lo que la complejidad es la multiplicacion de los tamaños de las 2 entradas.


# ----------------------------------------------------------------------------------------------


# 5. What is the time complexity in terms of O()?
# O(log_2(n))
# resumes is an array
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



## *** ANALISIS DE LA COMPLEJIDAD ** ##
# La complejidad es O(log_2(n)) ya que recorre el bucle y en la siguinete iteración, el tamaño se reduce a la mitad
# y según lo que demostramos en los ejercicios anteriores, el resultado es un log(n)

# ----------------------------------------------------------------------------------------------
