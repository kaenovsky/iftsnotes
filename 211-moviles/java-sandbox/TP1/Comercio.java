// Ejercicio 10 TP1

import java.util.Scanner;

public class Comercio {

	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);
		System.out.println("### Conocer las compras de un comercio ###");
        
        boolean res = true;
        int i = 0;
        int j = 1;
        String name = "";
        String itemName = "";
        double price = 0;
        int units = 0;
        double purchase = 0;
        double totalUser = 0;
        double totalShop = 0;

        while(res) {
            System.out.println("Ingrese cliente n° " + (i + 1));
            System.out.println("~~~~~~~~~~~~~~~~~~~");

            System.out.println("Nombre del cliente: ");
            name = scanner.nextLine();

            while(j == 1) {
                System.out.println("Nombre de producto comprado: ");
                itemName = scanner.nextLine();

                System.out.println("Precio del producto: ");
                price = scanner.nextDouble();

                System.out.println("Cantidad de artículos: ");
                units = scanner.nextInt();

                // Calc purchase

                purchase = units * price;
                totalUser = totalUser + purchase;

                System.out.println("Para continuar la carga de compras de " + name + " ingrese 1. Para finalizar ingrese 0.");
                int nextPurchase = scanner.nextInt();

                if(nextPurchase == 0) {
                    j = 0;
                }

            }

            // Calc total purchase from all clients
            totalShop = totalShop + totalUser;

            System.out.println("Para continuar ingresando empleados ingrese 1. Para finalizar ingrese 0.");
            int nextUser = scanner.nextInt();
            
            if(nextUser == 0) {
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
        System.out.println("Reporte compras del día"); 
        System.out.println("~~~~~~~~~~~~~~~~~~~");
        System.out.println("::: Total clientes " + i + " :::");
        System.out.println("~~~~~~~~~~~~~~~~~~~");
        System.out.println("La suma total de las compras del día es: $" + totalShop);        
	}

}