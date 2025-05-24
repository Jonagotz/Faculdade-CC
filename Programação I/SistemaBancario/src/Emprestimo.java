public class Emprestimo extends Servico {
    double valor;
    double taxa;

    public Emprestimo(String data, double valor, double taxa) {
        super(data);
        this.valor = valor;
        this.taxa = taxa;
    }

    public double calculaTaxa() {
        return this.valor * 0.1;
    }
}
