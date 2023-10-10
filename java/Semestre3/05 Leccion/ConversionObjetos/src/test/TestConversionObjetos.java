
package test;
import domain.*;
public class TestConversionObjetos {
    public static void main(String[] args) {
        Empleado empleado;
        empleado = new Escritor("Juan", 5000, TipoEscritura.CLASICO);
        System.out.println("empleado = " + empleado);
        System.out.println(empleado.obtenerDetalles());
        //empleado.getTipoEscritura(); No se puede hacer
        //Downcasting
        //((Escritor)empleado).getTipoEscritura();// primera opcion
        Escritor escritor = (Escritor)empleado;  //segunda opcion
        escritor.getTipoEscritura();
        
        //Upcasting
        Empleado empleado2 = escritor;
        System.out.println(empleado2.obtenerDetalles());
    }
}
