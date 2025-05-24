package Pacote;
public class Pedido{
    int indexItem = 0;
    private ItemPedido item[];
    private double valorTotal;

    public Pedido(){
        this.item = new ItemPedido[10000];
    }

    public void adicionarItem(ItemPedido it){
        this.item[indexItem] = it;
        indexItem++;
    }

    public void obterTotal(){
        valorTotal = 0.0;
        for (int i = 0; i < indexItem; i++) {
            ItemPedido itemPedido = item[i];
            Produto produto = itemPedido.getProd();
            int quantidade = itemPedido.getQtde();
            double valorItem = produto.getValor() * quantidade;
            valorTotal += valorItem;
        }
        System.out.println("Valor total do pedido: " + valorTotal);
    }
}