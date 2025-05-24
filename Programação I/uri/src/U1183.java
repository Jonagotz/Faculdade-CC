import java.util.Scanner;

public class U1183 {
    public static void main(String[] args) throws Exception {
        Scanner leitor = new Scanner(System.in);
        double soma = 0;
        char caracter = leitor.next().toUpperCase().charAt(0);
        double[][] vet = new double[12][12];

        for (int i = 0; i < vet.length; i++) {
        	for (int j = 0; j < vet[i].length; j++) {
        		vet[i][j] = leitor.nextDouble();
        	}
        }
        
        for (int i = 0; i < vet.length; i++) {
        	for (int j = 0; j < vet[i].length; j++) {
        		if (j > i) soma += vet[i][j];
        	}
        }

        if (caracter == 'M') soma /= ((vet.length * vet.length) - 12) / 2;
    	System.out.println(String.format("%.1f", soma));
        leitor.close();
    }
	
}
