# definindo as estruturas
estados = []
alfabeto = []
func_transicao = {}
estado_inicial = ""
estados_aceitacao = []

# recebendo os dados do automâto
print("Informe o conjunto de estados: ", end="")
estados = input().split()

print("Informe o alfabeto de estados: ", end="")
alfabeto = input().split()

print("Informe o estado inicial: ", end="")
estado_inicial = input()

print("Informe o conjunto de estados de aceitação: ", end="")
estados_aceitacao = input().split()

print("Defina as funções de transição: ")
for estado in estados:
    for simbolo in alfabeto:
        print(f"\t {simbolo}")
        print(f"{estado}\t ------>\t", end="")
        proximo_estado = input()

        if proximo_estado == ".":
            func_transicao[(estado, simbolo)] = None
        else: 
            func_transicao[(estado, simbolo)] = proximo_estado

# reconhecendo linguagens
print("Informe a linguagema a ser reconhecida: ", end="")
entrada = input()

estado_atual = estado_inicial

for simbolo in entrada:
    print(f"Estado atual: {estado_atual}")
    print(f"Simbolo atual: {simbolo}")
    print(f"Proximo estado: {func_transicao[(estado_atual, simbolo)]}")
    estado_atual = func_transicao[(estado_atual, simbolo)]

    if estado_atual == None:
        print("O autômato não reconheceu")
        break
if estado_atual in estados_aceitacao:
    print("Reconheceu")
else: 
    print("Não reconheceu")
