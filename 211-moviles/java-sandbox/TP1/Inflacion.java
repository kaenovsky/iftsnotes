// Ejercicio 8 TP1

import java.util.Scanner;
import java.util.HashMap;
import java.util.Collections;
import java.util.Map;

public class Inflacion {

	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);
		System.out.println("### Conocer el % de inflación de productos ###");
        
        boolean res = true;
        int i = 0;
        String product;
        double newPrice, oldPrice, inflation;
        HashMap<String, Double> map = new HashMap<>();

        while(res) {
            System.out.println("Ingrese producto n° " + (i + 1));
            System.out.println("~~~~~~~~~~~~~~~~~~~");

            System.out.println("Nombre del producto: ");
            product = scanner.nextLine();

            System.out.println("Precio anterior: ");
            oldPrice = scanner.nextDouble();

            System.out.println("Precio actual: ");
            newPrice = scanner.nextDouble();

            // Calc inflation rate
            inflation = ((newPrice - oldPrice) / oldPrice) * 100;

            // Add values to hash
            map.put(product, inflation);

            System.out.println("Para continuar la carga de artículos ingrese 1. Para finalizar ingrese 0.");
            int nextProd = scanner.nextInt();
            
            if(nextProd == 0) {
                res = false;
            }

            i++; // increment loop counter

            scanner.nextLine(); // consume line break

        }

        System.out.println("~~~~~~~~~~~~~~~~~~~");
        System.out.println("Fin carga de datos");
        System.out.println("~~~~~~~~~~~~~~~~~~~");

        // Show Report
        System.out.println("~~~~~~~~~~~~~~~~~~~");
        System.out.println("Reporte inflación de artículos"); 
        System.out.println("~~~~~~~~~~~~~~~~~~~");
        System.out.println("::: Total de artículos cargados: " + i + " :::");
        System.out.println("~~~~~~~~~~~~~~~~~~~");
        
        // Average inflation rate (sum all values)
        double sum = 0.0f;
        for (double f : map.values()) {
            sum += f;
        }

        System.out.println("Promedio de inflación: " + sum / i);

        // Find the max value of hashmap
        Double max = Collections.max(map.values());
        
        // Show the product name of max value
        for (Map.Entry<String, Double> entry : map.entrySet()) {
            if (entry.getValue() == max) {
                System.out.println("El producto con mayor inflación es: " + entry.getKey());
                System.out.println("El porcentaje de inflación es: " + entry.getValue() + "%");
            }
        }
        
	}

}