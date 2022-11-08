
package ejericicio04;

//import java.util.Scanner;
import javax.swing.JOptionPane;


public class Ejercicio04 {
    public static void main(String[] args) {
        //Scanner entrada = new Scanner(System.in);
        int numero, conteo = 0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("digite otro numero: "));
        while(numero >= 0){
            JOptionPane.showMessageDialog(null, "el numero "+numero+" es positivo");
            conteo++;
            System.out.println("digite otro numero: ");
            numero = Integer.parseInt(JOptionPane.showInputDialog("digite otro numero: "));
        }
        System.out.println("ha ingresado "+conteo+" numeros que no son negativos");
    }
}


