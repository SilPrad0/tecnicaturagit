
package test;

import domain.*;

public class TestInstanceOf {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Sil", 4500);
        determinarTipo(empleado1);
       // empleado1 = new Gerente("José", 5000, "Sistemas");
        //determinarTipo(empleado1);
    }
    
    // instance of
    
    public static void determinarTipo(Empleado empleado){  //metodo generico(imprimir) para imprimir info de varias clases
        if(empleado instanceof Gerente){
            System.out.println("es de tipo gerente");
            Gerente gerente = (Gerente)empleado;   //convierto empleado a tipo gerente y asi lo llamo
            gerente.getDepartamento();
        }
        else if (empleado instanceof Empleado){
            System.out.println("es de tipo empleado");
        }
        else if (empleado instanceof Object){
            System.out.println("es de tipo object");
        }
    }
    
    
}
