import java.util.Scanner;

public class U1065 {
    
    public static void main(String[] args) throws Exception {

        Scanner leitor = new Scanner(System.in);

        int contador = 0;
        int input;

        for (int i = 0; i < 5; i++){
            input = leitor.nextInt();
            if (input % 2 == 0) {
                contador ++;
            }
        }

        System.out.println(contador + " valores pares");

        leitor.close();
    }
}
