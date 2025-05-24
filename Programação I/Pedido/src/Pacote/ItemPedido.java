package Pacote;

public class ItemPedido {
    private Produto prod;
    private int qtde;

    public void setProd(Produto prod) {
        this.prod = prod;
    }

    public void setQtde(int qtde) {
        this.qtde = qtde;
    }

    public Produto getProd() {
        return prod;
    }

    public int getQtde() {
        return qtde;
    }

}
