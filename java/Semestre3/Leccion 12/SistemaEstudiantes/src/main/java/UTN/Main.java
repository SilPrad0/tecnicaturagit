package UTN;

import UTN.conexion.Conesxion;
public class Main {
    public static void main(String[] args) {
        var conexion = Conesxion.getConnection();
        if (conexion != null)
            System.out.println("conexion exitosa: " + conexion);
        else
            System.out.println("Error al conectarse");
    }
}