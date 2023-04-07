// Ejercicio 3 TP1

import java.util.Scanner;

public class Sueldos {

	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);
		System.out.println("### Conocer el sueldo por horas ###");
        
        boolean res = true;
        int i = 1;
        String name;
        float hours, hvalue, salary;

        while(res) {
            System.out.println("Ingrese empleado n° " + i);
            System.out.println("~~~~~~~~~~~~~~~~~~~");

            System.out.println("Nombre del empleado: ");
            name = scanner.nextLine();

            System.out.println("Horas trabajadas este mes: ");
            hours = scanner.nextFloat();

            System.out.println("Valor de hora en pesos: ");
            hvalue = scanner.nextFloat();

            salary = hvalue * hours;

            System.out.println("~~~~~~~~~~~~~~~~~~~");
            System.out.println("El sueldo que corresponde a " + name + " es de $" + salary);
            System.out.println("~~~~~~~~~~~~~~~~~~~");

            System.out.println("Para continuar ingresando empleados ingrese 1. Para finalizar ingrese 0.");
            int nextUser = scanner.nextInt();
            
            if(nextUser == 0) {
                res = false;
            }

            i++; // increment loop counter

            scanner.nextLine(); // consume line break

        }
	}

}