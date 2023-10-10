
package dominio;

public class Persona {
    //atributos
    private String nombre;
    private double sueldo;
    private boolean eliminado;
    
    //Constructor
    public Persona(String nombre, double sueldo, boolean eliminado){
        this.nombre = nombre;
        this.sueldo = sueldo;
        this.eliminado = eliminado; 
        
    }
    //metodos 

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public double getSueldo() {
        return sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    public boolean isEliminado() {  //en vez de get es is en bool para recup info
        return eliminado;
    }

    public void setEliminado(boolean eliminado) {
        this.eliminado = eliminado;
    }
    public String toString(){ //convierte en cadena a acada atributo
        return "Persona [nombre: "+this.nombre+
                ",sueldo: "+this.sueldo+
                ",eliminado: "+this.eliminado+"]";
    }
    
}
