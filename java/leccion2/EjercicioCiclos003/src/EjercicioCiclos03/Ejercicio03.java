
package EjercicioCiclos03;

//import java.util.Scanner;
import javax.swing.JOptionPane;


public class Ejercicio03 {
        public static void main(String[] args) {
        //Scanner entrada = new Scanner(System.in);
        int numero;
        System.out.println("digite un numero: ");
        numero = Integer.parseInt(JOptionPane.showInputDialog("digite un numero: "));
        while(numero != 0) {
            if(numero % 2 == 0){
                JOptionPane.showMessageDialog(null, "el numero ingresado "+numero+" es PAR"); 
            }
            else{
                JOptionPane.showMessageDialog(null, "el numero ingresado "+numero+" es impar");
            }
            System.out.println("digite otro numero");
            numero = Integer.parseInt(JOptionPane.showInputDialog("digite un numero: "));
        }
        System.out.println("el numero ingresado finaliza el programa");
    }
}


