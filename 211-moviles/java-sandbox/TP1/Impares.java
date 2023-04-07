// Ejercicio 1 TP1

import java.util.Scanner;

public class Impares {

	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);
		System.out.println("Ingrese un numero para saber si es par o impar:");
		int num = scanner.nextInt();

		if(num % 2 == 0) {
		
			System.out.println("El número es par");

		} else {
		
			System.out.println("El número es impar");

		}

	}

}