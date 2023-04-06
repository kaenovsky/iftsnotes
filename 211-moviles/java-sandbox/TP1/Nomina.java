// Ejercicio 5 TP1

import java.util.Scanner;
import java.util.ArrayList;

public class Nomina {

	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);
		System.out.println("### Conocer la nómina de empleados y sueldo Bruto ###");
        
        boolean res = true;
        int i = 0;
        String name;
        double netSalary, grossSalary;
        ArrayList<String> arrUsr = new ArrayList<String>();
        ArrayList<Double> arrGrs = new ArrayList<Double>();
        ArrayList<Double> arrNet = new ArrayList<Double>();

        while(res) {
            System.out.println("Ingrese empleado n° " + (i + 1));
            System.out.println("~~~~~~~~~~~~~~~~~~~");

            System.out.println("Nombre del empleado: ");
            name = scanner.nextLine();
            arrUsr.add(name);

            System.out.println("Salario neto este mes: ");
            netSalary = scanner.nextDouble();
            arrNet.add(netSalary);

            // Calc Gross Salary
            grossSalary = netSalary * 1.195;
            arrGrs.add(grossSalary);

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
        System.out.println("Reporte salarios"); 
        System.out.println("~~~~~~~~~~~~~~~~~~~");
        System.out.println("::: Total empleados " + i + " :::");

        int j = 0;
        while(i != j) {
            System.out.println("~~~~~~~~~~~~~~~~~~~");
            System.out.println("Empleado número: " + (j + 1));
            System.out.println("Nombre: " + arrUsr.get(j));
            System.out.println("Salario neto: " + arrNet.get(j));
            System.out.println("Salario bruto: " + arrGrs.get(j));
            System.out.println("~~~~~~~~~~~~~~~~~~~");
            j++;
        }
	}

}