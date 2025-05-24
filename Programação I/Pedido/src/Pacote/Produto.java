package Pacote;

public class Produto {
    
    private int codigo;
    private double valor;
    private String descr;

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public void setValor(double valor) {
        this.valor = valor;
    }

    public void setDescr(String descr) {
        this.descr = descr;
    }

    public int getCodigo() {
        return codigo;
    }

    public double getValor() {
        return valor;
    }

    public String getDescr() {
        return descr;
    }
}


