import java.util.Scanner;

public class Multiplos {

	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);
		System.out.println("### Debe ingresar dos números ###");
        
        Integer num1 = 0;
        Integer num2 = 0;

        // Ingreso de valores

        do {
            System.out.println("~~~ (!) Ingrese valores mayores a 0 ~~~");

            System.out.println("Ingrese número 1: ");    
            num1 = scanner.nextInt();

            System.out.println("Ingrese número 2: ");
            num2 = scanner.nextInt();
        }

        while((num1 <= 0) || (num2 <= 0));

        // Chequeamos si son múltiplos

        if(num1 % num2 == 0) {
            System.out.println("El número " + num1 + " es múltiplo de " + num2);
        } else {
            System.out.println("El número " + num1 + " NO es múltiplo de " + num2);
        }

	}

}