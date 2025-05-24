import java.util.Scanner;

import javax.swing.JOptionPane;

public class App {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Como pretende pagar? (1 - Cartão de Crédito, 2 - Cartão de Débito)");
        int a = input.nextInt();

        Cartao c;
        if (a == 1) {
            c = new CartaoCredito(); 
        } else {
            c = new CartaoDebito();
        }
        c.pagar(0);

        input.close();
    }
}
