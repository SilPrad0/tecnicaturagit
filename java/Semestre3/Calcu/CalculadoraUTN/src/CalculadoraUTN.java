import java.util.Scanner;

public class CalculadoraUTN {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("******* Calculadora *******");
        System.out.println("Digite un numero: ");
        var operando1 = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite un numero: ");
        var operando2 = Integer.parseInt(entrada.nextLine());
        var resultado = operando1 + operando2;
        System.out.println("resultado = "+resultado );
    }
}
