package presentacion;
import UTN.datos.EstudianteDao;
import UTN.dominio.Estudiante;
import java.util.Scanner;
public class SistEstudiantesApp {
    public static void main(String[] args) {
        var salir = false;
        var consola = new Scanner(System.in);
        var estudianteDao = new EstudianteDao();
        while(!salir){
            try {
                mostrarMenu();
                salir = ejecutarOpciones(consola, estudianteDao);
            } catch (Exception e){
                System.out.println("Error a ejecutar operacion: "+e.getMessage());
            }
        }
    }

    private static void mostrarMenu(){
        System.out.println("""
                ----- Sistema de estudiantes -----
                1. Listar estudiantes
                2. Buscar estudiantes
                3. Agregar estudiante
                4. Modificar estudiante
                5. Eliminar estudiante
                6. Salir
                Elige una opción: 
                """);
    }

    private static boolean ejecutarOpciones(Scanner consola, EstudianteDao estudianteDao){
        var opcion = Integer.parseInt(consola.nextLine());
        var salir = false;
        switch (opcion){
            case 1 -> {
                System.out.println("Listado: ");
                var estudiantes = estudianteDao.listar();
                estudiantes.forEach(System.out::println);
            }
            case 2 ->{
                System.out.println("Id de estudiante a buscar: ");
                var idEstudiante = Integer.parseInt(consola.nextLine());
                var estudiante = new Estudiante(idEstudiante);
                var encontrado = estudianteDao.buscarEstuPorId(estudiante);
                if(encontrado)
                    System.out.println("encontrado: "+estudiante);
                else System.out.println("no encontrado");
            }
            case 3 ->{
                System.out.println("Agrergar: ");
                System.out.println("Nombre: ");
                var nombre = consola.nextLine();
                System.out.println("apellido: ");
                var apellido = consola.nextLine();
                System.out.println("telefono: ");
                var telefono = consola.nextLine();
                System.out.println("email: ");
                var email = consola.nextLine();
            }
            case 4 ->{
                System.out.println("Modificar estudiante: ");
                System.out.println("Id: ");
                var idEstudiante = Integer.parseInt(consola.nextLine());
                System.out.println("nombre: ");
                var nombre = consola.nextLine();
                System.out.println("apellido");
                var apellido = consola.nextLine();
                System.out.println("telefono");
                var telefono = consola.nextLine();
                System.out.println("Email");
                var email = consola.nextLine();
                var estudiante = new Estudiante(idEstudiante, nombre, apellido, telefono, email);
                var modificado = estudianteDao.modificarEstudiante(estudiante);
                if(modificado)
                    System.out.println("estudiante modificado");
                else
                    System.out.println("no modificado");
            }
            case 5 ->{
                System.out.println("eliminar estudiante: ");
                System.out.println("Id: ");
                var idEstudiante = Integer.parseInt(consola.nextLine());
                var estudiante = new Estudiante(idEstudiante);
                var eliminado = estudianteDao.eliminarEstudiante(estudiante);
                if(eliminado)
                    System.out.println("eliminado");
                else
                    System.out.println("no eliminado");

            }
            case 6 -> {
                System.out.println("Bye");
                salir = true;
            }
            default -> System.out.println("Opcion incorrecta");
        }
        return salir;
    }
}
