import java.util.Scanner;

public class U1117 {
    public static void main(String[] args) {
        Scanner leitor = new Scanner(System.in);
        boolean validador = true;
        int contador = 0;
        double media = 0, total = 0;

        while (validador) {
            if (contador < 2) {
                double input = leitor.nextDouble();
            
                if (input >= 0.0 && input <= 10.0) {
                    total += input;
                    contador ++;
                } else {
                    System.out.println("nota invalida");
                }

            } else {
                validador = false;
            }

        }

        media = total / 2;

        System.out.printf("media = %.2f\n", media);

        leitor.close();
    }
}
