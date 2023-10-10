
package test;

import accesodatos.*;

public class TestInterface {
    public static void main(String[] args) {
        IAccesoDatos datos = new ImplementacionMySql();
     //datos.listar();    // " " desde mysql
      //imprimir(datos);    //llama al metodo de mysql
        
        datos = new ImplementacionOracle();
     //datos.listar();      //utilizo polimorfismo e implementa desde la clase oracle
        imprimir(datos);   // al metodo de oracle
    }
    
    public static void imprimir(IAccesoDatos datos){
        datos.listar();
    }
}
