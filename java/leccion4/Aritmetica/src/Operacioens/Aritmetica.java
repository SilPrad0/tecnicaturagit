package Operacioens;

public class Aritmetica {
    int a;
    int b;
    public void sumarNumeros() {
        int resultado = a + b;
        System.out.println("resultado" + resultado);

    }
    public int sumarConRetorno() {
        return a + b;
    }
    public int sumarConArgumentos(int arg1, int arg2) {
        this.a = arg1;  //el argumento a se asigna al atributo this.a
        this.b = arg2;
      //  return a + b;
      return this.sumarConRetorno();
    }
}
