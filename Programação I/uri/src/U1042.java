import java.util.Scanner;

public class U1042 {
    public static void main(String[] args) throws Exception {
        int i, j, aux;
        Scanner leitor = new Scanner(System.in);
        int n1 = leitor.nextInt();
        int n2 = leitor.nextInt();
        int n3 = leitor.nextInt();
    
        int[] arr1 = {n1, n2, n3};
        int[] arr2 = arr1;
        int tam = arr1.length;

        for(i = 0; i < tam; i++){
            for(j = 0; j < tam - 1 - i; j++){
                if(arr2[j] > arr2[j + 1]){
                    aux = arr2[j];
                    arr2[j] = arr2[j+1];
                    arr2[j+1] = aux;
                }
            }
        }

        for (i = 0; i < tam; i++) {
            System.out.print(arr2[i] + "\n");
        }

        System.out.println("");
        
        for (i = 0; i < tam; i++) {
            System.out.print(arr1[i] + "\n");
        }

        leitor.close();
    }
}
