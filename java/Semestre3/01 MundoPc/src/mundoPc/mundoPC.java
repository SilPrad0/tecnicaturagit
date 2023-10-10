package mundoPc;

import ar.com.system2023.mundopc.*;  //con el * importo todas las clases

public class mundoPC {

    public static void main(String[] args) {
        Monitor monitorHP = new Monitor("HP", 13); //importar la clase
        Teclado tecladoHP = new Teclado("Bluetooth", "HP");
        Raton ratonHP = new Raton("Bluetooth", "HP");
        Computadora computadoraHP = new Computadora("Computadora HP", monitorHP, tecladoHP, ratonHP);

        //Creamos otros objetos
        Monitor monitorGamer = new Monitor("Gamer", 32); //importar la clase
        Teclado tecladoGamer = new Teclado("Bluetooth", "Gamer");
        Raton ratonGamer = new Raton("Bluetooth", "Gamer");
        Computadora computadoraGamer = new Computadora("Computadora Gamer", monitorGamer, tecladoGamer, ratonGamer);
        Orden orden1 = new Orden();  // inicializo el arreglo vacio
        Orden orden2 = new Orden(); //nueva lista

        orden1.agregarComputadora(computadoraHP);
        orden1.agregarComputadora(computadoraGamer);

        orden2.agregarComputadora(computadoraHP);
        orden1.mostrarOrden();
        orden2.mostrarOrden();

    }
}
