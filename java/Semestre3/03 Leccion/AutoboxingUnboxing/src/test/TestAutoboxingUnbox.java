
package test;

public class TestAutoboxingUnbox {
    public static void main(String[] args) {
        int enteroPrim = 10;   //Tipo primitivo
        System.out.println("enteroPrim = " + enteroPrim);
        Integer entero = 10; //Tipo object con clase Integer
        System.out.println("entero = " + entero.toString());
        
        int entero2 = entero;
        System.out.println("entero2 = " + entero2);
    }
}
