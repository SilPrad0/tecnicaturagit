
package domain;

public class Gerente extends Empleado{
    private String departamento;
    
    public Gerente(String nombre, double sueldo, String departamento){
        super(nombre, sueldo);   //llamado al constructor de la clase padre
        this.departamento = departamento;  //inicializo el atributo
    }
    // @= anotacion, modifica el comportamiento de un metodo definido
    @Override   
    public String obtenerDetalles(){
         return super.obtenerDetalles()+", Departamento: "+this.departamento;
    }
}
