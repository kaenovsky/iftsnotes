// Ejercicio 4 TP1

import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

public class Promedio {

	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);
		System.out.println("### Obtener promedio, max y min ###");
        
        int i = 0;
        int n = 5; // size of my arrayList
        int total = 0;
        int valueMax;
        int valueMin;

        ArrayList<Integer> arrNumbs = new ArrayList<Integer>(n);

        while(i < n) {
            System.out.println("Ingrese un número entre 0 y 9999:");
            System.out.println("~~~~~~~~~~~~~~~~~~~");
            int num = scanner.nextInt();
            if((num < 0) || (num > 9999)) {
                System.out.println("(!) error: ingrese un número entre 0 y 9999.");
            } else {
                // agrego num a array
                arrNumbs.add(num);
                total = total + num;
                i++;
            }
        }

        // Calc & Display:
        
        System.out.println("La lista completa de números es: " + arrNumbs);
        System.out.println("El mayor número de la lista es: " + Collections.max(arrNumbs));
        System.out.println("El menor número de la lista es: " + Collections.min(arrNumbs));
        System.out.println("El número promedio de la lista es: " + total / n);

	}

}