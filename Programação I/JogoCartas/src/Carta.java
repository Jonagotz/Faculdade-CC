public class Carta {
    public String naipe;
    public String valor;

    public Carta(String naipe, String valor) {
        if (checagemNaipe(naipe) == false) {
            throw new RuntimeException("Naipe inválido ao criar uma carta");
        } else if (checagemValor(valor) == false) {
            throw new RuntimeException("Valor inválido ao criar uma carta");
        } else {
            this.naipe = naipe;
            this.valor = valor;
        }
    }

    public boolean checagemNaipe(String naipe) {
        if(naipe.equals("paus") || naipe.equals("copas") || naipe.equals("espadas") || naipe.equals("ouros")){
            return true;
        } else {
            return false;
        }
    }

    public boolean checagemValor(String valor) {
        if(valor.equals("A") || valor.equals("2") || valor.equals("3") || valor.equals("4") || valor.equals("5")
                || valor.equals("6") || valor.equals("7") || valor.equals("8") || valor.equals("9")
                || valor.equals("10") || valor.equals("J") || valor.equals("Q") || valor.equals("K")) {
            return true;
        } else {
            return false;
        }
    } 

    // Método para retornar a carta formatada
    public String toString() {
        return valor + " de " + naipe;
    }
}