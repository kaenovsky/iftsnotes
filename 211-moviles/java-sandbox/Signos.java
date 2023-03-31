import java.util.Scanner;

public class Signos {

	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);
		System.out.println("Ingrese un signo:");
		String signo = scanner.nextLine();

		if(signo.equals ("Escorpio") || signo.equals("escorpio")) {
		
			System.out.println("Es escorpio");

		} else {
		
			System.out.println("No es escorpio");

		}

	}

}