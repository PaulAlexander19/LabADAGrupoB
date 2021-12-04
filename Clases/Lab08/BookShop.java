package Clases.Lab08;

import java.util.Scanner;

public class BookShop {
    public static void main(String[] args) {
        // Entrada de datos
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // int n = 3;

        int maxPrice = sc.nextInt();
        // int maxPrice = 3;
        
        int[] price = new int[n+1];
        price[0] = 0;
        for (int i = 1; i <= n; i++) {
                price[i] = sc.nextInt();
            }
        // int[] price = {0,1,2,3};
            
        int[] pages = new int[n+1];
        pages[0] = 0;
        for (int i = 1; i <= n; i++) {
                pages[i] = sc.nextInt();
            }
            
        // int[] pages = {0,1,4,6};

        // System.out.println(n);

        // desarrollo del codigo
        int[][] k = new int[n+1][maxPrice+1];

        for (int i = 1; i <= maxPrice; i++) {
            for (int j = 1; j <= n; j++) {
                k[j][i] = k[j-1][i];
                if (i >= price[j]) {
                    k[j][i] = Math.max(k[j][i], k[j-1][i - price[j]] + pages[j]);
                }
            }
        }

        System.out.println(k[n][maxPrice]);

    }
}
