import java.util.Scanner;

public class U1075 {
    
    public static void main(String[] args) throws Exception {
        Scanner leitor = new Scanner(System.in);
        int input = leitor.nextInt();

        for (int i = 1; i < 10000; i++) {
            if (i % input == 2) {
                System.out.println(i);
            }
        }

        leitor.close();
    }
}
