
package test;
public class TestArreglos {
    public static void main(String[] args) {
        int edades [] = new int [3];   // tres elementos
     // declaramos variable           // instanciamos objeto de tipo object   
     // System.out.println("edades: "+ edades);
        
        edades[0] = 17;
        System.out.println("edades = " + edades[0]);
        edades[1] = 13;
        System.out.println("edades = " + edades[1]);
        edades[2] = 15;
        System.out.println("edades = " + edades[2]);
        
        for (int i =0; i < edades.length; i++){
            System.out.println("edades y sus elementos: "+i+": "+edades[i]);
        }
    }
}
