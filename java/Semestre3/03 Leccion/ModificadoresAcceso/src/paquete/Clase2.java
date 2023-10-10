
package paquete;

class Clase2{
    String atributoDefault = "atributo default";
    
   /* Clase2(){
        System.out.println("Constructor default");
    } */
    
    void metodoDefault(){
        System.out.println("Metodo default");
    }
    
    public Clase2(){
        super();
        this.atributoDefault = "modificacion del atrb default";
        System.out.println("atributoDefault = " + this.atributoDefault);
        this.metodoDefault();
    }
}
