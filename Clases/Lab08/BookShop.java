package Clases.Lab08;

import java.util.Scanner;

public class BookShop {
    public static void main(String[] args) {
        // Entrada de datos
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int maxPrice = sc.nextInt();
        int[] price = new int[n];
        for (int i = 0; i < n; i++) {
            price[i] = sc.nextInt();
        }

        int[] pages = new int[n];
        for (int i = 0; i < n; i++) {
            pages[i] = sc.nextInt();
        }
        // System.out.println(n);

        // desarrollo del codigo
        int[][] k = new int[n][maxPrice];

        for (int i = 1; i < n; i++) {
            for (int j = 1; j < maxPrice; j++) {
                k[i][j] = k[i][j - 1];
                if (j >= price[i]) {
                    k[i][j] = Math.max(k[i][j], k[i - price[i]][j - 1] + pages[i]);
                }
            }
        }

        System.out.println(k[n-1][maxPrice-1]);

    }
}
