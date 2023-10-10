
package ciclos12;

import javax.swing.JOptionPane;


public class Ciclos12 {
    public static void main(String[] args) {
        //Scanner entrada = new Scanner(System.in);
        long factorial = 1;
        //System.out.printIn("Digite un numero: ");
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        for(int i=1; i<=numero; i++){
            factorial *= i;
        }

    //System.out.println("\nEl factoriaal del nro ingresado es: "+factorial);
    JOptionPane.showMessageDialog(null, "El factorial de num ingresado es: "+factorial);
}
}
