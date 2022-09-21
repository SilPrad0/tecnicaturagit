/*leer un nro e indicar si es + o -, el proceso se repetirá hasta que se introduzca un cero con JopPane*/
package Ciclos02;

import javax.swing.JOptionPane;

public class Ejercicio02 {
    public static void main(String[] args) {
        var numero = Integer.parseInt(JOptionPane.showInputDialog("digite un numero: "));
        while(numero != 0) {
            if(numero > 0){
                System.out.println("El numero "+numero+" es positivo");
            }
            else{
            System.out.println("el numero "+numero+" es negativo");
        }
            numero = Integer.parseInt(JOptionPane.showInputDialog("digite otro numero: "));
        }
        System.out.println("El numero "+numero+" finaliza el programa");
    }
}
