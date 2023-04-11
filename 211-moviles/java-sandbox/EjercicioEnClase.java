import java.util.Scanner;

public class EjercicioEnClase {
    public static void main(String[] args) {

        saludar();
        System.out.println(saludarConReturn());
        System.out.println(saludarConReturnyParametros("Estoy saludando desde el parámetro saludoP"));
        calc();        

    }

    // Paso la función de Ale a un método:

    public static void calc() {
        int numero, acumulador = 0, contador = 0;
        float promedio = 0;

        Scanner leeEntradaPorTeclado = new Scanner(System.in);

        System.out.println("Cálculo de promedio de números entre 0 y 9999");

        do{

            System.out.println("Ingrese un número  entre 0 y 9999");
            numero = leeEntradaPorTeclado.nextInt();

            int numeroAlCuadrado = elevaAlCuadrado(numero);
            System.out.println(numeroAlCuadrado);

            if(numero < 0 || numero > 9999 ){
                System.out.println("El número ingresado será omitido...");
            }else{
                contador++;
                acumulador = numero + acumulador;
                promedio = acumulador/contador;
            }

            System.out.println("El promedio es: "+ promedio);

        }while(promedio < 9000);
    }

    //Métodos estáticos
    public static void saludar(){

        System.out.println("Estoy saludando desde Saludar");

    }

    public static String saludarConReturn(){

        String saludo = "Saludando con Return";

        return saludo;

    }

    public static String saludarConReturnyParametros(String saludoP){

        return saludoP;

    }

    public static int elevaAlCuadrado(int numeroaElevarP){

        int resultado = numeroaElevarP*numeroaElevarP;
        return resultado;

    }


}
