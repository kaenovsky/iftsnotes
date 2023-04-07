// Ejercicio 7 TP1

import java.util.Scanner;
import java.util.ArrayList;

public class Descuentos {

	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);
		System.out.println("### Listado de compradores y su descuento ###");
        
        boolean res = true;
        int i = 0;
        String name;
        int client;
        double subtotal, tons, price, discount;
        ArrayList<String> arrUsr = new ArrayList<String>();
        ArrayList<Double> arrSubTotal = new ArrayList<Double>();
        ArrayList<Double> arrDiscount = new ArrayList<Double>();

        while(res) {
            System.out.println("Ingrese cliente n° " + (i + 1));
            System.out.println("~~~~~~~~~~~~~~~~~~~");

            System.out.println("Nombre del cliente: ");
            name = scanner.nextLine();
            arrUsr.add(name);

            System.out.println("Cantidad de toneladas compradas: ");
            tons = scanner.nextDouble();

            System.out.println("Precio por tonelada: ");
            price = scanner.nextDouble();
            subtotal = price * tons;
            arrSubTotal.add(subtotal);

            System.out.println("Tipo de cliente (1, 2 o 3): ");
            client = scanner.nextInt();

            // Calc subtotal discount price
            switch(client) {
                case 1:
                    discount = subtotal * 0.05;
                    break;
                case 2:
                    discount = subtotal * 0.08;
                    break;
                case 3:
                    discount = subtotal * 0.12;
                    break;
                default:
		            discount = 0;
            }

            arrDiscount.add(discount);

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
        System.out.println("Reporte Compras"); 
        System.out.println("~~~~~~~~~~~~~~~~~~~");
        System.out.println("::: Total de compras cargadas " + i + " :::");

        int j = 0;
        while(i != j) {
            System.out.println("~~~~~~~~~~~~~~~~~~~");
            System.out.println("Cliente número: " + (j + 1));
            System.out.println("Nombre: " + arrUsr.get(j));
            System.out.println("Subtotal $" + arrSubTotal.get(j));
            System.out.println("Descuento $" + arrDiscount.get(j));
            System.out.println("Total $" + (arrSubTotal.get(j) - arrDiscount.get(j)));
            System.out.println("~~~~~~~~~~~~~~~~~~~");
            j++;
        }
	}

}