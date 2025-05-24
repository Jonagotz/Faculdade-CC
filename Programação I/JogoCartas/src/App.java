public class App {
    public static void main(String[] args) throws Exception {
        // Cria um baralho e embaralha as cartas:
        Baralho baralho = new Baralho();
        baralho.embaralhar();

        // Cria um vetor de cartas para representar a mão do jogador:
        Carta[] maoJogador = new Carta[7];

        // Pesca 7 cartas e adiciona elas na mão do jogador utilizando tratamento de exceções:
        try {
            for (int i = 0; i < 7; i++) {
                Carta carta = baralho.pescar();
                maoJogador[i] = carta;
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

        // Imprime as cartas que foram pescadas previamente caso nenhum erro tenha ocorrido:
        System.out.println("Cartas na mão:");
        for (Carta carta : maoJogador) {
            if (carta != null) {
                System.out.println(carta);
            }
        }
    }
}
