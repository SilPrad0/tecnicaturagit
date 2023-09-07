package test;

import enumeraciones.Continentes;
import enumeraciones.Dias;

public class Test_enumeraciones {
    public static void main(String[] args) {
      //  System.out.println("Dia 3: "+Dias.MIERCOLES);
     //   indicarDiaSemana(Dias.MIERCOLES);
        System.out.println("Continente No. 1: " + Continentes.ASIA);
        System.out.println("Nro paises: "+ Continentes.ASIA.getPaises());
    }
    
    private static void indicarDiaSemana(Dias dias){
        switch(dias){   // Convertimos switch a RULE SWITCH => mas cortito
            case LUNES -> System.out.println("Primer dia de la semana");
            case MARTES -> System.out.println("Segundo dia");
            case MIERCOLES -> System.out.println("Tercer dia");
            case JUEVES -> System.out.println("Cuarto dia");
            case VIERNES -> System.out.println("Quinto dia");
            case SABADO -> System.out.println("Sexto dia");
            case DOMINGO -> System.out.println("Septimo dia");
        }
    }
}
