
package test;

import domain.*;

public class TestSobreescritura {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Sil", 4500);
        imprimir(empleado1);
        //System.out.println("empleado1 = " + empleado1.obtenerDetalles());
        Gerente gerente1 = new Gerente("José", 5000, "Sistemas");
        imprimir(gerente1);
        //System.out.println("gerente1 = " + gerente1.obtenerDetalles());    
    }
    
    // polimorfismo
    
    public static void imprimir(Empleado empleado){  //metodo generico(imprimir) para imprimir info de varias clases
        System.out.println("empleado = " + empleado.obtenerDetalles());  //llama al metodo sobreescrito en la clase hija
    }
    
    
}
