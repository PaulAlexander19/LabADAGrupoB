package Clases.Lab03.Tarea;

public class App {
    public static void main(String[] args) {
        String[] mens = {"Victor", "William", "xavier", "Yancey", "Zeus"};
        String[] womens = {"Amy", "Bertha", "Claire", "Diane", "Erika"};
        
        int [][] preferenceMens = {{1,0,3,4,2},{3,1,0,2,4},{1,4,2,3,0},{0,3,2,1,4},{1,3,0,4,2}};
        int [][] preferenceWomens = {{4,0,1,3,2},{2,1,3,0,4},{1,2,3,4,0},{0,4,3,2,1},{3,1,4,2,0}};
        
        // String[] mens = {"Jorge", "Luis", "Mario"};
        // String[] womens = {"Ana", "Bea", "Clara"};
        
        // int [][] preferenceMens = {{0,1,2},{1,0,2},{0,1,2}};
        // int [][] preferenceWomens = {{1,0,2},{0,1,2},{0,1,2}};
        
        
        StableMaching s = new StableMaching(mens, womens, preferenceMens, preferenceWomens);
        s.match();
    }
}
