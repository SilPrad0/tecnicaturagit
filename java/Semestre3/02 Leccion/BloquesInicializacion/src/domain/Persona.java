package domain;

public class Persona {
    private final int idPersona;   //vars ?? 
    private static int contadorPersonas;
    
    static{      //bloque de inicializacion estatico
        System.out.println("Ejecucion del bloque estatico");
        ++Persona.contadorPersonas;
    }
    // bloque no estatico o dinamico, (solo se abren llaves)
    {
        System.out.println("Bloque dinamico");
        this.idPersona = Persona.contadorPersonas++;
}
    public Persona(){   //constructor
        System.out.println("Esta es la ejecucion del constructor");
    }
    public int getIdPersona(){     // el get
        return this.idPersona;
    }
}
