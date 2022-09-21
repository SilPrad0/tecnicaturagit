
package Clases;

public class Pruebapersonas {
    public static void main(String[] args) {
        Persona persona1;
        persona1 = new Persona();  //llamando al constructor 
        persona1.nombre = "Silvina";
        persona1.apellido = "Prado"; 
        persona1.obtenerInfo(); //metodo llamado
    }
}
