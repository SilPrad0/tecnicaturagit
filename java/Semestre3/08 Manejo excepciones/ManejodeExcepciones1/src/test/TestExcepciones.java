package test;

import aritmetica.Aritmetica;
import excepciones.OperacionExcepcion;

public class TestExcepciones {

    public static void main(String[] args) {
        int resultado = 0;
        try {
            resultado = Aritmetica.division(10, 0);
        } catch (OperacionExcepcion e) {
            System.out.println("Ocurrio un error de tipo OperacionExcepcion");
            System.out.println(e.getMessage());
        } catch (Exception e) {
            System.out.println("ocurrio un error");
            e.printStackTrace(System.out);  // imprime pila de excepciones
            System.out.println(e.getMessage());
        } finally {
            System.out.println("se realizo la division");   //siempre se ejecuta
        }
        System.out.println("Valor de resultado: " + resultado);
    }
}
