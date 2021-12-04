package Clases.Lab08;

// UniquePath.java
// @author: Paul Luque
// @description: Encontrar el numero de caminos para llegar el otro extremo de la matris, en la matris de obtavulos, el 1 es un obtaculo y no podemos pasar por ese lugar

public class UniquePath {
    public static void main(String[] args) {
        int[][] test = { { 0, 0, 0, 1 }, { 0, 1, 0, 1 }, { 0, 0, 0, 0 } };
        int resultado = 0;
        resultado = uniquePathsWithObstacles(test);
        System.out.println(resultado);
    }

    public static int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int[][] caminos = new int[obstacleGrid.length][obstacleGrid[0].length];
        for (int j = 0; j < obstacleGrid.length; j++) {
            for (int i = 0; i < obstacleGrid[j].length; i++) {
                // System.out.println(obstacleGrid[j][i]);

                // Verificacmos si esta bloqueado
                if (obstacleGrid[j][i] == 1) {
                    caminos[j][i] = 0;
                    continue;// finalizar
                }

                // Inicio del cuadro
                if (i - 1 < 0 && j - 1 < 0) {
                    caminos[j][i] = 1;
                    // lateral izquierdo
                } else if (i - 1 < 0) {
                    caminos[j][i] = caminos[j - 1][i]; // Sumamos el de arriba
                    // Superior
                } else if (j - 1 < 0) {
                    caminos[j][i] = caminos[j][i - 1]; // Sumamos el de la izquierda
                    // Cuadro normal
                } else {
                    caminos[j][i] = caminos[j - 1][i] + caminos[j][i - 1];

                }

            }

        }

        // imprimimos la matris "caminos"
        for (int j = 0; j < caminos.length; j++) {
            for (int i = 0; i < caminos[j].length; i++) {
                System.out.print(caminos[j][i] + " ");
            }
            System.out.println();
        }

        return caminos[obstacleGrid.length - 1][obstacleGrid[0].length - 1];
    }

}