
package Clases;

public class Pruebapersonas {
    public static void main(String[] args) {
        Persona persona1;
        persona1 = new Persona();  //llamando al constructor 
        persona1.nombre = "Silvina"; //el valor hexadecimal normalmente comienza con 0x
        persona1.apellido = "Prado"; 
        persona1.obtenerInfo(); //metodo llamado
        
        Persona persona2 = new Persona();
        System.out.println("persona2 = " + persona2);
        System.out.println("persona1 = " + persona1);
        persona2.obtenerInfo();
        persona2.nombre = "vero";
        persona2.apellido = "rodriguez";
        persona2.obtenerInfo();
        
        
        
    }
}
