package Operacioens;

public class PruebaAritmetica {
    public static void main(String[] args) {
       // int a = 10;
        //int b = 7;   //variables locales
        Aritmetica aritmetica1 = new Aritmetica();
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros();

        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado " + resultado);

        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("Resultado usando argumentos:  " + resultado);
        
        System.out.println("aritmetica1 a: "+aritmetica1.a);
        System.out.println("aritmetica1 b: "+aritmetica1.b);

        Aritmetica aritmetica2 = new Aritmetica(5,8);
        System.out.println("aritmetica2 = " + aritmetica2.a);
        System.out.println("aritmetica2 = " + aritmetica2.b);
        
      // Persona persona = new Persona("Silvina", "Prado");
        //System.out.println("persona = "+ persona);
        //System.out.println("Persona nombre: "+persona.nombre);
       // System.out.println("Persona apellido: "+ persona.apellido); 
        
    }
    //modularidad creamos un nuevo metodo
    public static void  miMetodo(){
       // a = 10;
        System.out.println("aca hoy otro metodo");
    }

    private static class string {

        public string() {
        }
    }
    class Persona{
        string nombre;
        string apellido;
        
        Persona(string nombre, string apellido){
           super();  //constructor vacio q no necesita argumentos clase Padre objetc
           //Imprimir imprimir = new Imprimir();
            new Imprimir().imprimir(this);
            this.nombre = nombre;
            this.apellido =apellido;
            System.out.println("objeto persona usando this: "+this);
        }
    }
    class Imprimir{
        public Imprimir(){
            super(); //el contrsc de la clase padre, para reservar memoria
           
        }
        public void imprimir(Persona persona){
            System.out.println("persona desde la clase imrpimir: "+persona);
            System.out.println("impresion del objeto actual (this): "+this);
        }
    }
}
