
package paquete;

import paquete2.Clase4;

public class TestDefault {
    public static void main(String[] args) {
        ClaseHija claseH = new ClaseHija();   //objeto
        claseH.atributoDefault = "otra modif del atr d";
        System.out.println(" claseH atributo default = " +  claseH.atributoDefault);
        
        Clase4 clase4 = new Clase4("publico");
        clase4.setAtributoPrivate("Cambio");   //accediendo al set
        System.out.println("clase4 = " + clase4.getAtributoPrivate());  // accediendo al get
        
    }
    
}
