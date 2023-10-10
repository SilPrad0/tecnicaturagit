package UTN.conexion;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Conesxion {
    public static Connection getConnection() {
        Connection conexion = null;
        // variables para conectarnos bd
        var baseDatos = "estudiantes";
        var url = "jdbc:mysql://localhost:3306/" + baseDatos;
        var usuario = "root";
        var password = "admin";

        // cargar clase del driver
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            conexion = DriverManager.getConnection(url, usuario, password);
        } catch (ClassNotFoundException | SQLException e) {
            System.out.println("Ocurrió un error en la conexion: " + e.getMessage());
        }  // fin catch
        return conexion;
    }  // fin metodo conexion

}
