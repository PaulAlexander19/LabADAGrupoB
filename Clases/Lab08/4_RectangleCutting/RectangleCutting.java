
import java.util.Scanner;

// RectangleCutting 
// @author: Paul Luque

public class RectangleCutting {

	public static void main(String[] args) {

		Scanner scan = new Scanner(System.in);
		// Recibiimos los datos
		int a = scan.nextInt();

		int b = scan.nextInt();

		scan.close();

		cuttingRectangle(a, b);

	}

	public static void cuttingRectangle(int a, int b) {

		// Creamos la estrucutra que en la quenos apoyaremos
		int[][] cut = new int[a + 1][b + 1];

		for (int rows = 1; rows < a + 1; rows++) {

			for (int cols = 1; cols < b + 1; cols++) {

				if (rows == cols) {

					cut[rows][cols] = 0;

				} else {

					int ans = Integer.MAX_VALUE;

					// Revisamos los cortes horizontale
					for (int i = 1; i < cols; i++) {

						ans = Math.min(ans, 1 + cut[rows][cols - i] + cut[rows][i]);

					}

					// Revisamos los cortes verticales
					for (int i = 1; i < rows; i++) {

						ans = Math.min(ans, 1 + cut[rows - i][cols] + cut[i][cols]);

					}

					// Devolvemos la ultima posicion dentro de nuestro rectangulo con
					// el minimo de cortes
					cut[rows][cols] = ans;

				}

			}

		}

		System.out.println(cut[a][b]);

	}

}