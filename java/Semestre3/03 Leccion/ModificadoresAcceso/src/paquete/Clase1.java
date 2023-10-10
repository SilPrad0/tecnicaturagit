
package paquete;

public class Clase1 {
    public String atributoPublic = "Valor atributo public";
    protected String atributoProtected = "Valor atributo protected";
    
    public Clase1(){
        System.out.println("Constructor public");
    }
    
    protected Clase1(String atributo){
        System.out.println("Constructor protected");
    }
    
    protected void metodoProtected(){
        System.out.println("Metodo protected");
    }
    
     public void metodoPublic(){
        System.out.println("Metodo public");
    }
}
