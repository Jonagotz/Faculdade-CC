import java.util.Collections;
import java.util.List;
import java.util.ArrayList;

public class Baralho {
    public List<Carta> pilhaCartas;

    public Baralho() {
        pilhaCartas = new ArrayList<>();
        String[] naipes = {"paus", "ouros", "copas", "espadas"};
        String[] valores = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"};

        for (String naipe : naipes) {
            for (String valor : valores) {
                pilhaCartas.add(new Carta(naipe, valor));
            }
        }
    }

    public void embaralhar() {
        Collections.shuffle(pilhaCartas);
    }

    public Carta pescar() throws Exception{
        if (pilhaCartas.isEmpty()) {
            throw new Exception("Baralho vazio, não é possível pescar mais cartas");
        }
        return pilhaCartas.remove(0);
    }
}