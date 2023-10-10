
package test;

import paquete.Clase1;
import paquete2.Clase3;

public class TestModAcceso {
    public static void main(String[] args) {
        Clase1 clase1 = new Clase1();   // llame a la clase publica
        System.out.println("clase1 = " + clase1.atributoPublic);  // al atributo publico
        clase1.metodoPublic();   // y al metodo 
        Clase3 claseHija = new Clase3();
        System.out.println("claseHija = " + claseHija);
    }
    
}
