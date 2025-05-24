import java.util.Scanner;

public class U1175 {
        public static void main(String[] args) throws Exception {
        Scanner leitor = new Scanner(System.in);
        int[] vet = new int[20];
        int i, j, aux;

        for (i = 0; i < 20; i++) {
            //vet[i] = (20 - i);

            int input = leitor.nextInt();
            vet[i] = input;
        }

        for (i = 0, j = 19; i < 10; i++, j--) {
            aux = vet[i];
            vet[i] = vet[j];
            vet[j] = aux;
        }

        for (i = 0; i < 20; i++) {
            System.out.println("N[" + i + "] = " + vet[i]);
        }

        leitor.close();
    }
}
