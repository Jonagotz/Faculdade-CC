import random

def AFD(A, cadeia):
    (Q, Sigma, delta, estado_inicial, estados_finais) = A
    qA = estado_inicial
    for jogada in cadeia:
        qA = delta[(qA, jogada)]
    return qA
#----------------------------------------------------------------
def definir_automato():
    # Estados: 
    #  q0 (inicial)
    #  q1 (empate)
    #  q2 (vitória jogador)
    #  q3 (vitória computador)
    Q = {"q0", "q1", "q2", "q3"}  
    
    # possibilidades de entrada
    Sigma = {("pedra", "pedra"), ("pedra", "papel"), ("pedra", "tesoura"),
             ("papel", "pedra"), ("papel", "papel"), ("papel", "tesoura"),
             ("tesoura", "pedra"), ("tesoura", "papel"), ("tesoura", "tesoura")}
    
    # Estado inicial
    estado_inicial = "q0"
    
    estados_finais = {"q1", "q2", "q3"}  

    # ("estado inicial", ("jogador", "computador")): "resultado"
    delta = {
        ("q0", ("pedra", "pedra")): "q1",
        ("q0", ("pedra", "papel")): "q3",
        ("q0", ("pedra", "tesoura")): "q2",
        ("q0", ("papel", "pedra")): "q2",
        ("q0", ("papel", "papel")): "q1",
        ("q0", ("papel", "tesoura")): "q3",
        ("q0", ("tesoura", "pedra")): "q3",
        ("q0", ("tesoura", "papel")): "q2",
        ("q0", ("tesoura", "tesoura")): "q1",
    }

    return (Q, Sigma, delta, estado_inicial, estados_finais)
#----------------------------------------------------------------
def joga(jogada_jogador, jogada_computador):
    A = definir_automato()
    cadeia = [(jogada_jogador, jogada_computador),(jogada_jogador, jogada_computador)]
    
    estado_final = AFD(A, cadeia)
    
    if estado_final == "q1":
        return "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠀\n⠀⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⠀\n⠀⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⠀\n⠀⣿⣿⣿⣿⡟⢀⣾⣿⣷⡖⠒⣀⣀⣤⣶⣾⣿⣷⣶⣤⣤⣴⣾⣆⠘⣿⣿⣿⠀\n⠀⣿⣿⣿⡿⠁⣾⣿⣿⣿⣧⣀⠙⠛⠛⠛⠋⣈⠻⢿⣿⣿⣿⣿⣿⣧⠈⢿⣿⠀\n⠀⣿⣿⣿⠁⣼⣿⠟⠻⠿⣿⣿⣿⣷⣶⣾⣿⠿⣷⣄⡉⠻⣿⣿⣿⣿⣧⠈⢿⠀\n⠀⠛⠛⠃⠀⠻⠋⣠⣶⠄⠙⠛⢻⣿⣿⣿⣷⣦⣈⠛⢿⣦⣄⠙⠻⠛⠁⠀⠀⠀\n⠀⠀⠀⠀⠀⢠⣾⠟⠁⣠⣿⠇⠈⠛⣿⣿⣈⠙⠿⣷⣦⡈⠛⠛⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠁⢠⣾⡿⠁⣠⣾⠆⠸⠉⠻⣷⣤⡈⠙⠿⠃⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⣾⠟⢁⣴⡶⠀⣤⡀⠙⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣿⠟⠁⠀⠛⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Empate!"
    elif estado_final == "q2":
        return "\n░░░░░░░░░░░░░░░░░░░░░░█████████░░░░░░░░░\n░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███░░░░░░░\n░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███░░░░\n░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░Você venceu!\n░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███░\n░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██\n░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██\n░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██\n░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██\n██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░\n░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░\n░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░░░░░\n░░████████████░░░█████████████████░░░░░░ Meus parabéns"
    elif estado_final == "q3":
        return "\n░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░\n░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░\n░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░\n░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░\n░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░\n░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░\n░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░\n█▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█\n█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█ O computador venceu!\n█░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█\n█░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█\n█░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█\n█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█\n░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░\n░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░\n░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░\n░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░\n░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░ Mais sorte na próxima"
    else:
        return "Erro na simulação."
#---------------------------------------------------------------- 
def valida_jogada(jogada):
    if jogada not in(["pedra", "papel", "tesoura"]):
        return "Jogada inválida"
#----------------------------------------------------------------
def main():
    print("Digite qual a jogada que deseja fazer, sendo elas 'pedra', 'papel' ou 'tesoura': ", end = "")
    jogada_jogador = input()
    # if valida_jogada(jogada_jogador) == "jogada inválida":
    #    return
    
    jogada_computador = random.choice(["pedra", "papel", "tesoura"])
    print(f"O computador jogou: {jogada_computador}")

    # Desfaça o comentário caso deseje controlar a escolha do computador
    print("Digite qual a jogada que deseja fazer, sendo elas 'pedra', 'papel' ou 'tesoura': ", end = "")
    jogada_computador = input()

    resultado = joga(jogada_jogador, jogada_computador)
    print(resultado)

main()