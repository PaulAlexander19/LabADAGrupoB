// @Autor: Luque Ccosi, Paul Alexander
// @Ejercicio: FindingBorders
// Lab 11

#include <stdio.h>
#include <string.h>

#define N 1000000

int main()
{
    static char cc[N + 1]; // cadena de caracteres a analizar
    static int zz[N];      // arreglo de longitudes de bordes
    int n, i, l, r;        

    scanf("%s", cc);                   // ingreso cadena
    n = strlen(cc);                    // longitud de cadena
    for (i = 1, l = r = 0; i < n; i++) 
        if (zz[i - l] < r - i)         // si el borde es menor que el borde derecho - indice
            zz[i] = zz[i - l];         // entonces se copia el borde izquierdo
        else
        {
            l = i;                              // actualizamos el indice izquierdo
            if (r < l)                          // si el borde derecho es menor que el borde izquierdo
                r = l;                          // entonces se actualiza el borde derecho
            while (r < n && cc[r] == cc[r - l]) // se busca el borde derecho
                r++;                            // actualizamos el borde derecho
            zz[i] = r - l;                      
        }
    for (i = n - 1; i > 0; i--)   // recorremos inversamente
        if (zz[i] == n - i)       
            printf("%d ", n - i); // imprime la longitud del borde
    printf("\n");                 
    return 0;                     
}