
package ar.com.system2023.mundopc;

public class Orden {
    private final int idOrden;
    private final Computadora computadora[]; //array de objetos
    private static int contadorOrdenes;
    private static final int MAX_COMPUTADORAS =10;
    private int contadorComputadora;
    
    //Constructor vacio
    public Orden(){
        this.idOrden = ++Orden.contadorOrdenes;
        this.computadora = new Computadora[Orden.MAX_COMPUTADORAS];
        
    }
    
    //Método para agregar una nueva pc al arreglo
    public void agregarComputadora(Computadora computadora){
        if(this.contadorComputadora < Orden.MAX_COMPUTADORAS){  //condicion 
            this.computadora[this.contadorComputadora++] = computadora;  //para agregar un elemento
        }
        else{
            System.out.println("has superado el limite: "+Orden.MAX_COMPUTADORAS);
        }
    }
    //metodo mostrar orden
    public void mostrarOrden(){
        System.out.println("Orden#:"+this.idOrden);
        System.out.println("Computadoras de la orden #: " +this.idOrden);
        for(int i = 0; i < this.contadorComputadora; i++){
            System.out.println(this.computadora[i]);
        }
    }
}
