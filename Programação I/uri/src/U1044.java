import java.util.Scanner;

public class U1044 {
    
    static void verifica(int a, int b){
        if (a % b == 0 || b % a == 0 ) {
            System.out.println("Sao Multiplos");
        } else {
            System.out.println("Nao sao Multiplos");
        }
    }

    public static void main(String[] args) throws Exception {

        Scanner leitor = new Scanner(System.in);
        
        int n1 = leitor.nextInt();
        int n2 = leitor.nextInt();

        verifica(n1, n2);

        leitor.close();
    }
}
