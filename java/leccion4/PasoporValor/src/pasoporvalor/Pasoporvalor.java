
package pasoporvalor;

public class Pasoporvalor {
    public static void main(String[] args) {
        var valorx = 20;
        System.out.println("valorx = " + valorx);
        cambioValor(valorx); // solo le enviamos una copia
    }
    public static void cambioValor(int arg1){
        System.out.println("arg1 = " + arg1);
        arg1 = 23; 
        
    }
}
