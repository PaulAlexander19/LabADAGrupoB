
public class MaximalSquare {

// MaximalSquare 
// @author: Paul Luque

    public static void main(String[] args) {

        // Caso de prueba
        char[][] matrix = { { '1', '0', '1', '0', '0' },
                { '1', '0', '1', '1', '1' },
                { '1', '1', '1', '1', '1' },
                { '1', '0', '0', '1', '0' } };

        System.out.println(maximalSquare(matrix));

    }

    public static int maximalSquare(char[][] matrix) {

        int rows = matrix.length;

        if (rows == 0) {

            return 0;

        }

        int cols = matrix[0].length;

        // Estructura de apoyo
        int[][] board = new int[rows + 1][cols + 1];

        int biggest = 0;

        // Iteramos los posiciones del rectangulo
        for (int i = 1; i < rows + 1; i++) {

            for (int j = 1; j < cols + 1; j++) {

                if (matrix[i - 1][j - 1] == '1') {

                    board[i][j] = 1 + Math.min(board[i - 1][j], Math.min(board[i][j - 1], board[i - 1][j - 1]));

                    if (biggest < board[i][j]) {

                        biggest = board[i][j];

                    }

                }

            }

        }

        return biggest * biggest;

    }

}