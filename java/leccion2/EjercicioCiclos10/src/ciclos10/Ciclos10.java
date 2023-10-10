//pedir diez numeros y sumarlos
package ciclos10;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ciclos10 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, suma = 0;
        for(int i = 1; i <= 10; i ++){
            //System.out.println("Digite un numero: ");
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
            suma += numero;
        }
        //System.out.println("\nLa suma de los nros es: "+suma);
        JOptionPane.showMessageDialog(null, "La suma de los nros es: "+suma);
    }
}
