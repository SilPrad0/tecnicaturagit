
package test;


public class TestArgumVariables {
    public static void main(String[] args) {
        imprimirNumeros(3, 4, 5);  //le paso los argumentos
        imprimirNumeros(2, 3, 5);
        variosParametros("Silvina", 4, 5, 6);
    }
    
    private static void variosParametros(String nombre, int ...numeros){
        System.out.println("Nombre: "+ nombre);
        imprimirNumeros(numeros);
        
    }
    
    private static void imprimirNumeros(int ...numeros){
        for (int i = 0; i < numeros.length; i++) {
            System.out.println("Elementos: "+numeros[i]);
        }
        
    }
}
