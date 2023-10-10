package pasoporeferencia;

import Clases.Persona;

public class PasoPorReferencia {

    public static void main(String[] args) {
        Persona persona1 = new Persona();
        persona1.nombre = "sil";
        System.out.println("persona1 nombre = " + persona1.nombre);
        cambiarValor(persona1);
        System.out.println("el cambio que hicimos en el nombre es: " + persona1.nombre);
        persona1 = cambiarElValor(persona1);
        Persona persona2 = new Persona();
       //Persona persona2 = null;
        persona2 = cambiarElValor(persona2);
        System.out.println("el nuevo valor del obj es: " + persona2.nombre);
    }

    public static void cambiarValor(Persona persona) {
        persona.nombre = "Selva";
    }

    public static Persona cambiarElValor(Persona persona) {
        if (persona == null) {
            System.out.println("valor de persona invalido: Null");
            return null;
        } else {
            persona.nombre = "daniela";
            return persona;
        }
    }
}
