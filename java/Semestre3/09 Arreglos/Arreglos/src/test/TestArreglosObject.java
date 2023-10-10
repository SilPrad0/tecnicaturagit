
package test;

import domain.Persona;

public class TestArreglosObject {
    public static void main(String[] args) {
        Persona personas [] = new Persona[2];
        personas[0] = new Persona("silvina");
        personas[1] = new Persona("grogu");
        System.out.println("personas = 1" + personas[1]);
    }
}
