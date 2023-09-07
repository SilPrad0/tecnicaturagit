
package enumeraciones;

public enum Continentes {
    AFRICA(53, "e"),
    EUROPA(36, "2"),
    ASIA(44, "45"),
    AMERICA(34, "6"),
    OCEANIA(14, "5678");
    
    private final int paises; //atributo? encapsulado
    private final String habitantes;
    
    Continentes(int paises, String habitantes){ //constructor
        this.paises = paises;
        this.habitantes = habitantes;
    }
    
    //Metodo get para acceder al atrib encapsulado
    public int getPaises(){
        return this.paises;
    }
    public String getHabitantes(){
        return this.habitantes;
    }
}
