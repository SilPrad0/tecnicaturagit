
package caja;

public class PruebaCaja {
    public static void main(String[] args) {
        //var locales
        int medidaAncho = 3; //valores ingresados en codigo duro
        int medidaAlto = 2;
        int medidaProf = 6;
        
        Caja caja1 = new Caja();  //instanciamos objeto, constructor vacio
        caja1.ancho = medidaAncho; //pasamos valores al objeto
        caja1.alto = medidaAlto;
        caja1.profundo = medidaProf;
        int resultado = caja1.calcularVolumen(); //llamo al metodo
        //primer rtdo
        System.out.println("resultado volumen caja 1: " + resultado);
         
        Caja caja2 = new Caja(2, 4, 6); //lalmamos al constr2 con nuevos argumentos
        //llamamos con el nuevo objeto al metodo para un nuevo calculo
        System.out.println("resultado de volumen de la caja2: " + caja2.calcularVolumen());
    }
}
