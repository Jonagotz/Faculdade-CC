import java.util.Scanner;

public class U1064 {
    
    public static void main(String[] args) throws Exception {
    
        Scanner leitor =  new Scanner(System.in);
        int contador = 0;
        double media = 0;
        double input;

        for (int i = 0; i < 6; i++){
            input = leitor.nextDouble();
            if (input > 0) {
                contador ++;
                media += input;
            }
        }

        media = media / contador;
        System.out.println(contador + " valores positivos");
        System.out.println(String.format("%.1f", media));
        leitor.close();
    }
}
