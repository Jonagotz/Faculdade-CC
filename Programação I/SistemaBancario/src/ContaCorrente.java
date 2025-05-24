public class ContaCorrente extends Conta {
    private double limite;

    public ContaCorrente(int numero, double saldo, double limite) {
        super(numero, saldo);
        this.limite = limite;
    }
    
    public void emiteExtratoDetalhado() {
        // Implementar
    }

    public void aumentaLimite(double valor) {
        if (valor < 0) {
            throw new RuntimeException("Valor negativo inválido!");
        }

        this.limite += valor;
    }

    @Override
    public String toString() {
        return "ContaCorrente [limite=" + limite + "]";
    }

    
}
