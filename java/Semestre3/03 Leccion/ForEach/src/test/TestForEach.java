package test;

import domain.Persona;

public class TestForEach {
    public static void main(String[] args) {
        int edades[] = {5, 6, 7, 9};   //sintaxis resumida
        for (int edad: edades){ //sintaxis del forEach
            System.out.println("edad = " + edad);
        }
        
        Persona personas[] = {new Persona("Sil"), new Persona("pepe"), new Persona("Paque")};
        
        //For Each array tipo object
        for(Persona persona: personas){
            System.out.println("persona = " + persona);
        }
        
    }
}
