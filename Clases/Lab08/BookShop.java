package Clases.Lab08;

import java.util.Scanner;

// BookShop 
// @author: Paul Luque
// @description: Elegir el maximo numero de paginas que puedes comprar con un valor del precio maximo.

public class BookShop {
    public static void main(String[] args) {
        // Entrada de datos
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // int n = 3;

        int maxPrice = sc.nextInt();
        // int maxPrice = 3;
        
        int[] price = new int[n];
        // price[0] = 0;
        for (int i = 0; i < n; i++) {
                price[i] = sc.nextInt();
            }
        // int[] price = {0,1,2,3};
            
        int[] pages = new int[n+1];
        // pages[0] = 0;
        for (int i = 0; i < n; i++) {
                pages[i] = sc.nextInt();
            }
            
        // int[] pages = {0,1,4,6};

        // System.out.println(n);

        // desarrollo del codigo
        int[][] k = new int[n+1][maxPrice+1];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= maxPrice; j++) {
                k[i+1][j] = k[i][j];
                if (j >= price[i]) {
                    k[i+1][j] = Math.max(k[i + 1][j], pages[i] + k[i][j - price[i]]);
                }
            }
        }

        System.out.println(k[n][maxPrice]);

    }
}
