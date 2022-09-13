package Ciclos01;

import javax.swing.JOptionPane;

public class ejercicio01 {
    public static void main(String[] args) {
        int numero, cuadrado;
       
        numero = Integer.parseInt(JOptionPane.showInputDialog("digite un numero"));
        while(numero >= 0) { //mientras el numero sea igual a cero o positivo/mayor
            cuadrado = (int) Math.pow(numero, 2);
            System.out.println("El numero "+numero+" elevado al cuadrado es: "+cuadrado);
            numero = Integer.parseInt(JOptionPane.showInputDialog("digite otro numero"));
        }
        System.out.println("El programa ha finalizado por numero negativo");
    }
    
}
