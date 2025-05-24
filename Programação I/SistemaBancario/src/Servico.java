public class Servico {
    Cliente cliente;
    String dataContratacao;

    public Servico(String data) {
        this.dataContratacao = data;
    }

    public double calculaTaxa() {
        return 10;
    }
}
