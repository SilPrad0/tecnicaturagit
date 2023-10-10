
package paquete2;

public class Clase4 {
    private String atributoPrivate = "atributo private";
    
    
    private Clase4(){
        System.out.println("Constructor private");
        
    }
    //creamos un constructor public para poder crear objetos
    public Clase4(String argumento){   //podemos llamar al constructor vacio aca
        this();
        System.out.println("Constructor publico");
    }
    
    
    private void metodoPrivado(){
        System.out.println("Metodo privado");
    }

    public String getAtributoPrivate() {
        return atributoPrivate;
    }

    public void setAtributoPrivate(String atributoPrivate) {
        this.atributoPrivate = atributoPrivate;
    }
    
    
}
