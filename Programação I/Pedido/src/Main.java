import Pacote.Pedido;
import Pacote.Produto;
import Pacote.ItemPedido;

public class Main {

    public static void main(String[] args) {
        // Criando objetos Produto
        Produto produto1 = new Produto();
        produto1.setCodigo(1);
        produto1.setValor(10.99);
        produto1.setDescr("Produto 1");

        Produto produto2 = new Produto();
        produto2.setCodigo(2);
        produto2.setValor(5.99);
        produto2.setDescr("Produto 2");

        // Criando objetos ItemPedido
        ItemPedido item1 = new ItemPedido();
        item1.setProd(produto1);
        item1.setQtde(3);

        ItemPedido item2 = new ItemPedido();
        item2.setProd(produto2);
        item2.setQtde(2);

        // Criando objeto Pedido
        Pedido pedido = new Pedido();
        pedido.adicionarItem(item1);
        pedido.adicionarItem(item2);

        pedido.obterTotal();
    }
}
