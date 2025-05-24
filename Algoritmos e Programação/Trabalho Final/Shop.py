# Cadastrar novos clientes
class usuarios:
    nome = None
    cpf = None
    email = None
    senha = None
    limitecredito = None
    balanço = None  # como em dinheiro não emprestado
    cartãonumero = None
    cartãosenha = None
    lista_carrinho = []
    total_carrinho = 0

# Cadastrar novos produtos


class produtos:
    numero = None
    nome = None
    valor = 0.0
    marca = None
    origem = None  # praqueles que não querem comprar da china

# Cria produtos


def cria_produtos(lista_produtos):
    # produto1
    pastad_oral = produtos()
    pastad_oral.numero = 1
    pastad_oral.nome = "Pasta de dente Oral-B"
    pastad_oral.valor = 5.99
    pastad_oral.marca = "Oral-B"
    pastad_oral.origem = "Estados Unidos"
    lista_produtos.append(pastad_oral)
    # produto2
    pastad_colgate = produtos()
    pastad_colgate.numero = 2
    pastad_colgate.nome = "Pasta de dente Colgate"
    pastad_colgate.valor = 3.99
    pastad_colgate.marca = "Colgate"
    pastad_colgate.origem = "Estados Unidos"
    lista_produtos.append(pastad_colgate)
    # produto3
    arroz_1kg = produtos()
    arroz_1kg.numero = 3
    arroz_1kg.nome = "Arroz 1kg"
    arroz_1kg.valor = 8.76
    arroz_1kg.marca = "João Ferro"
    arroz_1kg.origem = "Belo Horizonte"
    lista_produtos.append(arroz_1kg)
    # produto4
    arroz_2kg = produtos()
    arroz_2kg.numero = 4
    arroz_2kg.nome = "Arroz 2kg"
    arroz_2kg.valor = 15.89
    arroz_2kg.marca = "João Ferro"
    arroz_2kg.origem = "Belo Horizonte"
    lista_produtos.append(arroz_2kg)
    # produto5
    macarrao_500g = produtos()
    macarrao_500g.numero = 5
    macarrao_500g.nome = "Macarrão 500g"
    macarrao_500g.valor = 10.00
    macarrao_500g.marca = "galo"
    macarrao_500g.origem = "Peru"
    lista_produtos.append(macarrao_500g)
    # produto6
    macarrao_1kg = produtos()
    macarrao_1kg.numero = 6
    macarrao_1kg.nome = "Macarrão 1kg"
    macarrao_1kg.valor = 18.99
    macarrao_1kg.marca = "galo"
    macarrao_1kg.origem = "Peru"
    lista_produtos.append(macarrao_1kg)
    # produto7
    açucar_500g = produtos()
    açucar_500g.numero = 7
    açucar_500g.nome = "Açucar 500g"
    açucar_500g.valor = 9.99
    açucar_500g.marca = "Good Life"
    açucar_500g.origem = "Africa do Sul"
    lista_produtos.append(açucar_500g)
    # produto8
    açucar_1kg = produtos()
    açucar_1kg.numero = 8
    açucar_1kg.nome = "Açucar 1kg"
    açucar_1kg.valor = 20.00
    açucar_1kg.marca = "Good Life"
    açucar_1kg.origem = "Africa do Sul"
    lista_produtos.append(açucar_1kg)
    # produto9
    feijão_200g = produtos()
    feijão_200g.numero = 9
    feijão_200g.nome = "Feijão 200g"
    feijão_200g.valor = 8.25
    feijão_200g.marca = "Ô Feijim"
    feijão_200g.origem = "Rio Grande do Sul"
    lista_produtos.append(feijão_200g)
    # produto10
    feijão_1kg = produtos()
    feijão_1kg.numero = 10
    feijão_1kg.nome = "Feijão 1kg"
    feijão_1kg.valor = 18.79
    feijão_1kg.marca = "Ô Feijin"
    feijão_1kg.origem = "Rio Grande do Sul"
    lista_produtos.append(feijão_1kg)
    # produto11
    frango_sassami = produtos()
    frango_sassami.numero = 11
    frango_sassami.nome = "Frango Sassami"
    frango_sassami.valor = 23.89
    frango_sassami.marca = "Sadia"
    frango_sassami.origem = "Santa Catarina"
    lista_produtos.append(frango_sassami)
    # produto12
    carne_boi = produtos()
    carne_boi.numero = 12
    carne_boi.nome = "Filé Mignon kg"
    carne_boi.valor = 53.00
    carne_boi.marca = "Friboi"
    carne_boi.origem = "Goiás"
    lista_produtos.append(carne_boi)
    # produto13
    cafe_pilao = produtos()
    cafe_pilao.numero = 13
    cafe_pilao.nome = "Café 200g"
    cafe_pilao.valor = 5.89
    cafe_pilao.marca = "Pilão"
    cafe_pilao.origem = "África"
    lista_produtos.append(cafe_pilao)
    # produto14
    cafe_pilao1kg = produtos()
    cafe_pilao1kg.numero = 14
    cafe_pilao1kg.nome = "Café 1kg"
    cafe_pilao1kg.valor = 18.00
    cafe_pilao1kg.marca = "Pilão"
    cafe_pilao1kg.origem = "África"
    lista_produtos.append(cafe_pilao1kg)
    # produto15
    farinha_100g = produtos()
    farinha_100g.numero = 15
    farinha_100g.nome = "farinha de rosca 100g"
    farinha_100g.valor = 4.99
    farinha_100g.marca = "Rosa Branca"
    farinha_100g.origem = "Goiás"
    lista_produtos.append(farinha_100g)
    # produto16
    extrato_tomate = produtos()
    extrato_tomate.numero = 16
    extrato_tomate.nome = "Extrato de tomate 200g"
    extrato_tomate.valor = 10.99
    extrato_tomate.marca = "Calore"
    extrato_tomate.origem = "Argentina"
    lista_produtos.append(extrato_tomate)
    # produto17
    azeite = produtos()
    azeite.numero = 17
    azeite.nome = "Azeite extravirgem 500ml"
    azeite.valor = 12.50
    azeite.marca = "O-Live"
    azeite.origem = "Estados Unidos"
    lista_produtos.append(azeite)
    # produto18
    agua_sgas = produtos()
    agua_sgas.numero = 18
    agua_sgas.nome = "Água s/gás 500ml"
    agua_sgas.valor = 2.99
    agua_sgas.marca = "Naturágua"
    agua_sgas.origem = "Chapecó"
    lista_produtos.append(agua_sgas)
    # produto19
    coca_1l = produtos()
    coca_1l.numero = 19
    coca_1l.nome = "Coca-Cola 1,5L"
    coca_1l.valor = 13.99
    coca_1l.marca = "Coca-Cola"
    coca_1l.origem = "Estados Unidos"
    lista_produtos.append(coca_1l)
    #produto20 - último
    coca_2l = produtos()
    coca_2l.numero = 20
    coca_2l.nome = "Coca-Cola 2L"
    coca_2l.valor = 18.00
    coca_2l.marca = "Coca-Cola"
    coca_2l.origem = "Estados Unidos"
    lista_produtos.append(coca_2l)
    '''lista terminada de produtos'''

# 1 - Cadastro do cliente


def cadastramento(lista_usuarios):
    usuario = usuarios()
    while True:
        # pedindo nome
        usuario.nome = str(input("digite o seu Nome: "))
        # pedindo senha de acesso
        aux = True
        while aux == True:
            Senha = input(
                "Digite a senha para sua conta de até 6 caracteres: ")
            if len(Senha) > 6:
                print("Senha muito grande, tente uma menor")
                continue
            else:
                aux = False
        # pedindo cpf
        aux = True
        numTem = 0
        while aux == True:
            try:
                Cpf = input("Digite o seu CPF: ")
                cpf = Cpf.replace(".", "").replace("-", "")
                if cpf.count("0") == 11 or len(
                        cpf) != 11:  # Zero vezes algo sempre vai dar zero e o CPF vai ser considerado como vdd
                    print("CPF Inválido!")
                    continue

                soma_a = 0
                for i in range(9):
                    # Faz a primeira conta do digito verificador
                    soma_a += int(cpf[i]) * (10 - i)
                if (soma_a % 11) < 2:
                    soma_a = 0
                else:
                    soma_a = 11 - soma_a % 11
                cpf_valido = cpf.replace(cpf[9], str(soma_a))

                soma_b = 0
                for x in range(10):
                    # Faz a segunda conta do digito verficiador
                    soma_b += int(cpf_valido[x]) * (11 - x)
                if (soma_b % 11) < 2:
                    soma_b = 0
                else:
                    soma_b = 11 - soma_b % 11

                cpf_valido = cpf_valido.replace(cpf_valido[-1], str(soma_b))
                if cpf != cpf_valido:  # Verifica se o cpf digitado é válido
                    print("CPF Inválido!")
                    continue
                else:
                    cpf_format = cpf[0:3] + "." + cpf[3:6] + \
                        "." + cpf[6:9] + "-" + cpf[9:11]
                    aux = False
                    continue

            except (ValueError, IndexError):
                print("CPF Inválido!")
                continue

        # pedindo email
        aux = True
        numTem = 0
        while aux == True:
            Email = input("Digite o seu email: ")
            numTem += 1
            if "@" not in Email or Email in lista_usuarios or ".com" not in Email:
                print(
                    "Email invalido ou já cadastrado, por favor digite um Email válido")
                continue
            elif numTem > 3:
                print("Número de tentativas excedido, tente novamente mais tarde!")
                break
            else:
                aux = False
        # pedindo numero do cartão
        numTem = 0
        aux = True
        while aux == True:
            numTem += 1
            Cartão = input("Digite os numeros do cartão (16 caracteres): ")
            if len(Cartão) != 16:
                print("Numero invalido")
                continue
            elif numTem > 3:
                print("Número de tentativas excedido, tente novamente mais tarde!")
                break
            else:
                aux = False
        # pedindo senha do cartão
        numTem = 0
        aux = True
        while aux == True:
            numTem += 1
            Senha_Cartão = input("Digite a senha do cartão(4 caracteres): ")
            if len(Senha_Cartão) != 4:
                print("Senha invalida")
                continue
            elif numTem > 3:
                print("Número de tentativas excedido, tente novamente mais tarde!")
                break
            else:
                aux = False
        # pedindo limite de crédito existente
        aux = True
        while aux == True:
            LimiteCredito = float(
                input("Digite o seu limite de credito atual: "))
            if LimiteCredito > 1000:
                print("Opção de saldo inválido")
                continue
            else:
                aux = False
        #LimiteCredito = -LimiteCredito
        Balanço = 0
        usuario.cpf = Cpf
        usuario.email = Email
        usuario.senha = Senha
        usuario.limitecredito = LimiteCredito
        usuario.balanço = 0
        usuario.cartãonumero = Cartão
        usuario.cartãosenha = Senha_Cartão
        lista_usuarios.append(usuario)
        return True

# 2 - Consultar cliente


def consulta_cliente(lista_usuarios):
    cpf_consulta = input("Digite o CPF: ")
    for usuario in lista_usuarios:
        if cpf_consulta == usuario.cpf:
            print(f"\nO nome do cliente é {usuario.nome}")
            print(f"O email do cliente é {usuario.email}\n")
        else:
            print()

# 3 - Login


def login(lista_usuarios, usuario_logado, nivel_de_permissão):
    while True:
        for i in range(len(lista_usuarios)):
            Email = input("Digite o seu email: ")
            if Email == lista_usuarios[i].email or Email == "AdminSuperFoda@gmail.com":
                Senha = input("Digite a sua senha: ")
                for j in range(len(lista_usuarios)):
                    if Senha == lista_usuarios[i].senha and Email == "AdminSuperFoda@gmail.com":
                        print(
                            f"\nBem vindo(a) Admin {lista_usuarios[i].nome}!\n")
                        usuario_logado.nome = lista_usuarios[i].nome
                        usuario_logado.cpf = lista_usuarios[i].cpf
                        usuario_logado.email = lista_usuarios[i].email
                        usuario_logado.senha = lista_usuarios[i].senha
                        usuario_logado.limitecredito = lista_usuarios[i].limitecredito
                        usuario_logado.balanço = lista_usuarios[i].balanço
                        usuario_logado.cartãonumero = lista_usuarios[i].cartãonumero
                        usuario_logado.cartãosenha = lista_usuarios[i].cartãosenha
                        usuario_logado.lista_carrinho = lista_usuarios[i].lista_carrinho
                        nivel_de_permissão.append(2)
                        return lista_usuarios, usuario_logado, nivel_de_permissão
                    elif Senha == lista_usuarios[i].senha:
                        print(f"\nBem vindo(a) {lista_usuarios[i].nome}!\n")
                        usuario_logado.nome = lista_usuarios[i].nome
                        usuario_logado.cpf = lista_usuarios[i].cpf
                        usuario_logado.email = lista_usuarios[i].email
                        usuario_logado.senha = lista_usuarios[i].senha
                        usuario_logado.limitecredito = lista_usuarios[i].limitecredito
                        usuario_logado.balanço = lista_usuarios[i].balanço
                        usuario_logado.cartãonumero = lista_usuarios[i].cartãonumero
                        usuario_logado.cartãosenha = lista_usuarios[i].cartãosenha
                        usuario_logado.lista_carrinho = lista_usuarios[i].lista_carrinho
                        nivel_de_permissão.append(1)
                        return lista_usuarios, usuario_logado, nivel_de_permissão
                    elif Senha != lista_usuarios[i].senha:
                        print("Senha incorreta")
                        continue
            else:
                print("Esse email está incorreto e/ou não cadastrado")
                continue


# 4 - Compra
def compra(usuario_logado):
    produto_comprar = int(
        input("Digite  numero do produto que gotaria de comprar: "))
    if produto_comprar <= len(usuario_logado.lista_carrinho) + 1:
        produto_comprar -= 1
        variavel_temporaria_pra_testar_limite_credito = usuario_logado.balanço
        variavel_temporaria_pra_testar_limite_credito -= usuario_logado.lista_carrinho[produto_comprar].valor
        if variavel_temporaria_pra_testar_limite_credito >= usuario_logado.limitecredito:
            usuario_logado.balanço = variavel_temporaria_pra_testar_limite_credito
            print(
                f"Produto {usuario_logado.lista_carrinho[produto_comprar].nome}comprado com sucesso! Ele chegará a você em até 14 dias.")
            tira_do_carrinho = input(
                "Deseja retirar o produto de seu carrinho? Digite 'sim' para confirmar: ")
            if tira_do_carrinho.upper() == "SIM":
                usuario_logado.lista_carrinho.remove(
                    usuario_logado.lista_carrinho[produto_comprar])
                print("\nProduto removido do carrinho com sucesso.")
            else:
                print("\nO produto não foi removido")
        else:
            print("Você esta sem crédito no momento, para adicionar mais crédito escolha a opção 'Adicionar dinheiro' no menu inicial.")
            return
    else:
        print("Esse produto não se encontra na lista. Tente novamente")
        return

# 5 - Carrinho de compras


def Add_Carrinho(usuario_logado, lista_usuarios, lista_produtos):
    aux = True
    while aux == True:
        selecione_produto = int(input(
            "digite o numero do produto que deseja adicionar ou aperte '-1' para voltar ao menu: "))
        if selecione_produto == -1:
            print("\nVoltando para o menu\n")
            return
        if selecione_produto <= len(lista_produtos) + 1:
            for produtos in usuario_logado.lista_carrinho:
                if produtos.numero == selecione_produto:
                    print("Ele ja se encontra no carrinho")
                    continue
            # pra ir nos produtos certos, ja que o cliente não sabe que a listagem começa em "0"
            selecione_produto -= 1
            if selecione_produto < 0:
                print("Numero inválido")
                continue
            print(
                f"{lista_produtos[selecione_produto].nome} por R${lista_produtos[selecione_produto].valor:.2f}")
            BotaNoCarrinho = input(
                "Deseja depositar esse produto no carrinho? Digite 'sim' para confirmar, caso não queira digite 'nao': ")
            if BotaNoCarrinho.upper() == "SIM":
                print(
                    f"Produto {lista_produtos[selecione_produto].nome} adicionado ao carrinho")
                usuario_logado.lista_carrinho.append(
                    lista_produtos[selecione_produto])
                usuario_logado.total_carrinho += lista_produtos[selecione_produto].valor
            else:
                print("Produto não adicionado.")
                continue
        else:
            print("Numero invalido.")

# 9 Carrinho de compras


def listar_carrinho(usuario_logado):
    for produtos in usuario_logado.lista_carrinho:
        print(f"{produtos.nome} por R${produtos.valor}")
    print(f"Total: {usuario_logado.total_carrinho}")
    print()


# 6 Lista produtos


def listar_produtos(lista_produtos):
    for produtos in lista_produtos:
        print(produtos.numero, end=". ")
        print(produtos.nome, end=" da marca ")
        print(f"'{produtos.marca}'", end=" fabricado em ")
        print(produtos.origem, end=" por ")
        print(f"R${produtos.valor:.2f}")
        print()
    print()

# 7 adicionar credito


def adicionar_balanço(usuario_logado):
    chances_pra_senha = 3
    while chances_pra_senha >= 0:
        confirmar_a_senha = input("Digite a senha do seu cartão de credito: ")
        if confirmar_a_senha == usuario_logado.cartãosenha:
            mais_balanço = float(
                input("Digite o quando de dinheiro deseja adicionar: "))
            usuario_logado.balanço += mais_balanço
            print(
                f"Ordem realiazada com sucesso! Você agora tem R${usuario_logado.balanço:.2f} na sua conta")
            return usuario_logado
        elif confirmar_a_senha != usuario_logado.cartãosenha and chances_pra_senha > 1:
            chances_pra_senha -= 1
            print(
                f"Essa senha está incorreta, tente novamnete. {chances_pra_senha} tentativas restantes")
        elif chances_pra_senha == 1:
            print("tentativas esgotadas.")
            return
        else:
            print("returnando ao menu...")
            return

# 8 Adicione Produto: (admin only)


def novo_produto(lista_produtos):
    produto = produtos()
    adicione_produto_nome = input(
        "Digite o numero do novo produto e seu nome: ")
    adicione_produto_marca = input("Digite a marca do novo produto: ")
    for i in range(len(lista_produtos)):
        if adicione_produto_nome == lista_produtos[i].nome and adicione_produto_marca == lista_produtos[i].marca:
            print("Esse produto ja existe")
            continue
        else:
            confirme = input(
                f"Você está adicionando o produto {adicione_produto_nome} da marca '{adicione_produto_marca}', deseja continuar? Digite 'sim' para confirmar ou 'não' para retornar': ")
            if confirme.upper() == "SIM":
                produto.nome = adicione_produto_nome
                produto.marca = adicione_produto_marca
                produto.valor = float(
                    input("Digite o preço do novo produto: "))
                produto.origem = input("Digite a origem do novo produto: ")
                lista_produtos.append(produto)
                print(
                    f"Produto {adicione_produto_nome} da marca {adicione_produto_marca} adicionado pelo valor de R${produto.valor}")
                return lista_produtos
            elif confirme.upper() == "NAO":
                print("Produto não adicionado")
                return
            else:
                continue

# new novo produto


def novo_produtosssssssss(lista_produtos):
    produto = produtos()
    produto.numero = int(input("Digite o numero do novo produto: "))
    for i in range(len(lista_produtos)):
        if produto.numero == lista_produtos[i].numero:
            print("Esse produto ja existe")
            return
    produto.nome = input("Digite o nome do novo produto: ")
    produto.marca = input("Digite a marca do novo produto: ")
    confirme = input(
        f"Você está adicionando o produto {produto.nome} da marca '{produto.marca}', deseja continuar? Digite 'sim' para confirmar ou 'não' para retornar': ")
    if confirme.upper() == "SIM":
        produto.valor = float(input("Digite o preço do novo produto: "))
        produto.origem = input("Digite a origem do novo produto: ")
        lista_produtos.append(produto)
        print(
            f"Produto {produto.nome} da marca {produto.marca} adicionado pelo valor de R${produto.valor}")
        return lista_produtos
    else:
        return

# Menu principal


def menu():
    opcao = "-1"
    usuario_logado = usuarios()
    lista_usuarios = []
    lista_produtos = []
    nivel_de_permissão = [0]
    while True:
        opcao = input("Olá, Seja bem vindo! Esse é o menu principal, escolha dentre as seguinte opções:\n\n1- Cadastro\n2- Consultar cliente\n3- Login\n4- Compra\n5- Adicionar produtos ao carrinho\n6- Catálogo de produtos\n7- Adicionar dinheiro\n8- Adicionar item\n9- Carrinho de compras\n0- Sair\n")
        if opcao == "1":
            print("Opção selecionada: Cadastro")
            if cadastramento(lista_usuarios):
                print("\nCadastro realizado com sucesso\n")

        elif opcao == "2":
            print("Opção selecionada: Consultar cliente\n")
            consulta_cliente(lista_usuarios)

        elif opcao == "3":
            if nivel_de_permissão[-1] == 0:
                print("Opção selecionada: Login\n")
                login(lista_usuarios, usuario_logado, nivel_de_permissão)
            elif nivel_de_permissão[-1] != 0:
                are_you_sure = input(
                    "Tem certeza? Usar essa opção fará você sair de sua conta atual. Digite 'sim' para confirmar ou 'nao' para continuar na sessão atual: \n")
                if are_you_sure.upper() == "SIM":
                    print("Opção selecionada: Login\n")
                    login(lista_usuarios, usuario_logado, nivel_de_permissão)
                elif are_you_sure.upper() == "NAO":
                    continue

        elif opcao == "4":
            if nivel_de_permissão[-1] != 0:
                if len(usuario_logado.lista_carrinho) > 0:
                    print("Opção selecionada: Compra\n")
                    listar_carrinho(usuario_logado)
                    compra(usuario_logado)
                else:
                    print(
                        "Você não tem nada na seu carrinho! Adicione algo a ele para acessar essa opção.")
            else:
                print("Faça o login para acessar essa opção\n")

        elif opcao == "5":
            if nivel_de_permissão[-1] != 0:
                print("Opção selecionada: Adicionar produtos ao carrinho\n")
                if len(lista_produtos) == 0:
                    cria_produtos(lista_produtos)
                listar_produtos(lista_produtos)
                listar_carrinho(usuario_logado)
                Add_Carrinho(usuario_logado, lista_usuarios, lista_produtos)
            else:
                print("Faça o login para acessar essa opção\n")

        elif opcao == "6":
            if nivel_de_permissão[-1] != 0:
                print("Opção selecionada: Ver catálogo de produtos\n")
                if len(lista_produtos) == 0:
                    cria_produtos(lista_produtos)
                listar_produtos(lista_produtos)
            else:
                print("Faça o login para acessar o catálogo\n")

        elif opcao == "7":
            if nivel_de_permissão[-1] != 0:
                print("Opção selecionada: Adicionar Dinheiro\n")
                adicionar_balanço(usuario_logado)
            else:
                print("Faça o login para acessar essa opção\n")

        elif opcao == "8":
            if nivel_de_permissão[-1] == 2:
                print("Opção selecionada: Adicionar item\n")
                if len(lista_produtos) == 0:
                    cria_produtos(lista_produtos)
                listar_produtos(lista_produtos)
                novo_produtosssssssss(lista_produtos)
                listar_produtos(lista_produtos)
            elif nivel_de_permissão[-1] == 1:
                print("Essa opção é somente para admins\n")
            elif nivel_de_permissão[-1] == 0:
                print("Faça o login para acessar essa opção\n")

        elif opcao == "9":
            if nivel_de_permissão[-1] != 0:
                print("Opção selecionada: Carrinho de compras\n")
                if usuario_logado.total_carrinho == 0:
                    print("Carrinho vazio\n")
                else:
                    listar_carrinho(usuario_logado)
            else:
                print("Faça o login para acessar essa opção\n")

        elif opcao == "0":
            print("Opção selecionada: Sair")
            break

        else:
            print("Opção inválida, tente novamente\n")


menu()

# email de administrador = AdminSuperFoda@gmail.com
