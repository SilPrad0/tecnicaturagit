
package test;
import dominio.Persona; 

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("yo", 200000.00, false);
        
        //modificar a traves de metodos
        persona1.setNombre("Silvina");
        //acceder
        System.out.println("nombre: " +persona1.getNombre());
        System.out.println("sueldo: " +persona1.getSueldo());
        System.out.println("eliminado o no: " +persona1.isEliminado());
        System.out.println("persona1: "+persona1.toString());
        imprimir(persona1);
        
    }
    
    public static void imprimir(Persona persona){
        System.out.println("persona = " + persona);
    }
}