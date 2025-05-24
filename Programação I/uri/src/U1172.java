import java.util.Scanner;

public class U1172 {
    public static void main(String[] args) throws Exception {
        Scanner leitor = new Scanner(System.in);
        int[] arr = new int[10];

        for (int i = 0; i < arr.length; i++) {
            int input = leitor.nextInt();
            if (input <= 0) {
                input = 1;    
            }
            arr[i] = input;
        }

        for (int i = 0; i < arr.length; i++) {
            System.out.println("X[" + i + "] = " + arr[i]);
        }

        leitor.close();
    }
}
