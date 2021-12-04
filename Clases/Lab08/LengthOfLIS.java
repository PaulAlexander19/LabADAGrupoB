import java.util.Arrays;

// Length of LIS
// @author: Paul Luque
// @date: 09/03/2018
// @description: Find the length of the longest increasing subsequence in an array.

public class LengthOfLIS {
    public int lengthOfLIS(int[] nums) {

        // verificamos que el arreglo no este vacio
        if (nums == null || nums.length == 0) {
            return 0;
        }
        int len = nums.length;
        // creamos la estructura de apoyo
        int[] dp = new int[len];
        // inicializamos el arreglo de apoyo con 1
        Arrays.fill(dp, 1);
        int max = 1;
        // recorremos el arreglo
        for (int i = 1; i < len; i++) {
            for (int j = 0; j < i; j++) {
                // verificamos la posibilidade de una subsecuencia
                if (nums[i] > nums[j]) {
                    // Obtamos por la subsecuencia la longitud mas larga
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
            // Actualizamos el retorno 
            max = Math.max(max, dp[i]);
        }
        return max;
    }

}
