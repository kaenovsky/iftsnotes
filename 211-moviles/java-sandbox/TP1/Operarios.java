// Ejercicio 9 TP1

import java.util.Scanner;
import java.util.HashMap;
import java.util.Collections;
import java.util.Map;

public class Operarios {

	public static void main(String[] args) {

	    Scanner scanner = new Scanner(System.in);
	    System.out.println("### Conocer el listado de operarios y su productividad ###");
        
        boolean res = true;
        int i = 0;
        String name;
        // ppd = products per day
        int ppd;
        int maxppd = 0;
        int minppd = 1000000000;
        int totalppd = 0;
        int j = 1;
        HashMap<String, Integer> mapMax = new HashMap<>();
        HashMap<String, Integer> mapMin = new HashMap<>();

        while(res) {
            System.out.println("Ingrese Operario n° " + (i + 1));
            System.out.println("~~~~~~~~~~~~~~~~~~~");

            System.out.println("Nombre del Operario: ");
            name = scanner.nextLine();

            System.out.println("Ingrese de a uno los productos por día producidos por " + name);
            System.out.println("Ingrese -1 para finalizar con los productos de " + name +  " y continuar con el siguiente operario.");
            
            while(j == 1) {
                ppd = scanner.nextInt();
                
                if(ppd == -1) {
                    j = 0;
                } else {
                    totalppd = totalppd + ppd;
                    if(ppd > maxppd) {
                        maxppd = ppd;
                        mapMax.put(name, maxppd);
                    }
                    if(ppd < minppd) {
                        minppd = ppd;
                        mapMin.put(name, minppd);
                    }
                }
            }

            // reset ppd while variable
            j = 1;

            System.out.println("Para continuar la carga de operarios ingrese 1. Para finalizar ingrese 0.");
            int nextOp = scanner.nextInt();
            
            if(nextOp == 0) {
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
        System.out.println("Reporte Productividad Operarios"); 
        System.out.println("~~~~~~~~~~~~~~~~~~~");
        System.out.println("::: Total de operarios cargados: " + i + " :::");
        System.out.println("~~~~~~~~~~~~~~~~~~~");

        System.out.println("Promedio de productos producidos por día: " + totalppd / i);
        
        // Show the worker name with max value of ppd
        for (Map.Entry<String, Integer> entry : mapMax.entrySet()) {
            if (entry.getValue() == maxppd) {
                System.out.println("El operario con mayor productividad es: " + entry.getKey());
                System.out.println("Su mayor día de producción logró: " + entry.getValue() + " productos.");
            }            
        }

        // Show the worker name with min value of ppd
        for (Map.Entry<String, Integer> entry : mapMin.entrySet()) {
            if (entry.getValue() == minppd) {
                System.out.println("El operario con menor productividad es: " + entry.getKey());
                System.out.println("Su menor día de producción logró: " + entry.getValue() + " productos.");
            }            
        }
        
	}

}