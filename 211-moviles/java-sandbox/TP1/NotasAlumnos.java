// Ejercicio 6 TP1

import java.util.Scanner;
import java.util.ArrayList;

public class NotasAlumnos {

	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);
		System.out.println("### Alumnos y resultado de notas ###");
        
        boolean res = true;
        int i = 0;
        String name;
        double note1, note2, note3, total, avg;
        int pass = 0;
        int fail = 0;

        while(res) {
            System.out.println("Ingrese nombre del alumno n° " + (i + 1) + " y sus 3 notas.");
            System.out.println("~~~~~~~~~~~~~~~~~~~");

            System.out.println("Nombre del alumno: ");
            name = scanner.nextLine();

            System.out.println("Primera nota obtenida: ");
            note1 = scanner.nextDouble();

            System.out.println("Segunda nota obtenida: ");
            note2 = scanner.nextDouble();

            System.out.println("Tercera nota obtenida: ");
            note3 = scanner.nextDouble();

            // Calc if pass or fail
            total = note1 + note2 + note3;
            avg = total / 3;

            if(avg >= 4 ) {
                System.out.println("~~~~~~~~~~~~~~~~~~~");
                System.out.println("Alumno: " + name + " (Aprobado)");
                System.out.println("~~~~~~~~~~~~~~~~~~~");
                pass = pass + 1;
            } else {
                System.out.println("~~~~~~~~~~~~~~~~~~~");
                System.out.println("Alumno: " + name + " (Desaprobado)");
                System.out.println("~~~~~~~~~~~~~~~~~~~");
                fail = fail + 1;
            }

            System.out.println("Para continuar ingresando alumnos ingrese 1. Para finalizar ingrese 0.");
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
        System.out.println("Reporte notas alumnos"); 
        System.out.println("~~~~~~~~~~~~~~~~~~~");
        System.out.println("::: Total alumnos cargados " + i + " :::");
        System.out.println("~~~~~~~~~~~~~~~~~~~");
        System.out.println("Total de alumnos aprobados: " + pass);
        System.out.println("Total de alumnos desaprobados: " + fail);
        
	}

}