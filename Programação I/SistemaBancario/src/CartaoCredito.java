public class CartaoCredito extends Cartao {
    public String bandeira;
    public int cvv;

    public void pagar (double valor) {
        System.out.println("Pagar da classe Credito");
    }
}