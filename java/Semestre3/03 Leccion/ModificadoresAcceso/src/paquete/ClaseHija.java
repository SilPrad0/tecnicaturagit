
package paquete;

public class ClaseHija extends Clase2{
    public ClaseHija(){
        super();
        this.atributoDefault = "modificacion atributo default";
        System.out.println("atributoDefault = " + this.atributoDefault);
        this.metodoDefault();
    }
}
