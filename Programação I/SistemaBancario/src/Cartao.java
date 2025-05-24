public abstract class Cartao {
    private Cliente cliente;
    private Conta conta;

    public abstract void pagar (double valor);
}
