CPF = None
senha = None

def cadastroUsuario():
    CPF = input("Digite o seu CPF: ")

    while True:
        senha = input("Digite a sua senha: ")

        if len(senha) == 6 and senha.isdigit():
            break
        else:
            print("A senha deve conter 6 números. Digite novamente.")

    nome = input("Digite o seu nome: ")

    reais = 580.00
    bitcoin = 0.0158
    ethereum = 1.03
    ripple = 200.35

    bd = open("bd.txt", "a")
    bd.write(f"{CPF},{nome},{senha},{reais},{bitcoin},{ethereum},{ripple}\n")
    print("Cadastrado")

usuariologado = {
    "CPF": None,
    "nome": None,
    "senha": None
}





def loginUsuario():
    CPF = input("Digite o seu CPF: ")
    senha = input("Digite a sua senha: ")
    bd = open("bd.txt")

    try:
        for linha in bd:
            CPFbd, nome, senhabd, reais, bitcoin, ethereum, ripple = linha.strip().split(",")
            
            if CPF == CPFbd and senha == senhabd:
                print(f"Olá, {nome}!")
                usuariologado["CPF"] = CPF
                usuariologado["nome"] = nome
                usuariologado["senha"] = senhabd
                menuGeral()
                return
        print("CPF ou senha incorretos.")

    except FileNotFoundError:
        print("O arquivo de registros não foi encontrado.")





def consultarSaldo():
    senha = input("Digite a sua senha: ")

    if senha != usuariologado["senha"]:
        print("Senha incorreta. Tente novamente.")
        menuGeral()
        return
    
    bd = open("bd.txt", "r")
    for linha in bd:
        CPFbd, nome, senhabd, reais, bitcoin, ethereum, ripple = linha.strip().split(",")

        if senha == senhabd:
            print("Seu saldo: \n")
            print(f"Nome: {nome}")
            print(f"CPF: {CPFbd}")
            print(f"Reais: {float(reais):.2f}")
            print(f"Bitcoin: {float(bitcoin):.4f}")
            print(f"Ethereum: {float(ethereum):.2f}")
            print(f"Ripple: {float(ripple):.2f}")
            bd.close()
            return

    bd.close()





def consultarExtrato():
    pass





def depositar():
    senha = input("Digite a sua senha: ")

    if senha != usuariologado["senha"]:
        print("Senha incorreta. Tente novamente.")
        menuGeral()
        return

    valordeposito = float(input("Digite qual o valor do depósito: "))

    with open("bd.txt", "r") as bd:
        linhas = bd.readlines()

    with open("bd.txt", "w") as bd:
        for linha in linhas:
            CPFbd, nome, senhabd, reais, bitcoin, ethereum, ripple = linha.strip().split(",")

            if CPFbd == usuariologado["CPF"]:
                
                novosaldoreais = float(reais) + valordeposito
                
                print("Depósito realizado com sucesso.")

                bd.write(f"{CPFbd},{nome},{senhabd},{novosaldoreais},{bitcoin},{ethereum},{ripple}\n")

                print("Seu saldo atualizado:\n")
                print(f"Nome: {nome}")
                print(f"CPF: {CPFbd}")
                print(f"Reais: {float(novosaldoreais):.2f}")
                print(f"Bitcoin: {float(bitcoin):.4f}")
                print(f"Ethereum: {float(ethereum):.2f}")
                print(f"Ripple: {float(ripple):.2f}")
            else:
                bd.write(linha) # reescreve o registro dos outros usuários





def sacar():
    senha = input("Digite a sua senha: ")

    if senha != usuariologado["senha"]:
        print("Senha incorreta. Tente novamente.")
        menuGeral()
        return

    valorsaque = float(input("Digite o valor que deseja sacar: "))

    with open("bd.txt", "r") as bd:
        linhas = bd.readlines()

    with open("bd.txt", "w") as bd:
        for linha in linhas:
            CPFbd, nome, senhabd, reais, bitcoin, ethereum, ripple = linha.strip().split(",")

            if CPFbd == usuariologado["CPF"]:
                saldo = float(reais)

                if saldo < valorsaque:
                    print(f"Você não possui saldo suficiente. Seu saldo: {saldo:.2f}")
                    bd.write(linha)  # escreve a linha original sem alterações
                    menuGeral()
                else:
                    novosaldo = saldo - valorsaque
                    print(f"\nSaque realizado com sucesso.")

                    bd.write(f"{CPFbd},{nome},{senhabd},{novosaldo},{bitcoin},{ethereum},{ripple}\n")

                    print("Seu saldo atualizado:\n")
                    print(f"Nome: {nome}")
                    print(f"CPF: {CPFbd}")
                    print(f"Reais: {float(novosaldo):.2f}")
                    print(f"Bitcoin: {float(bitcoin):.4f}")
                    print(f"Ethereum: {float(ethereum):.2f}")
                    print(f"Ripple: {float(ripple):.2f}")
            else:
                bd.write(linha) # reescreve o registro dos outros usuários





def comprarCripto():
    pass





def venderCripto():
    pass





def atualizarCotacao():
    pass





def sair():
    print("Saindo...")
    exit





def menuGeral():
    opcoes = {
         "1.": "Consultar saldo",
         "2.": "Consultar extrato",
         "3.": "Depositar",
         "4.": "Sacar",
         "5.": "Comprar criptomoedas",
         "6.": "Vender criptomoedas",
         "7.": "Atualizar cotação",
         "8.": "Sair",
    }

    for numero, opcao in opcoes.items():
        print(f"{numero} {opcao}")

    opcao = input()

    if opcao == "1":
        consultarSaldo()
    elif opcao == "2":
        consultarExtrato()
    elif opcao == "3":
        depositar()
    elif opcao == "4":
        sacar()
    elif opcao == "5":
        comprarCripto()
    elif opcao == "6":
        venderCripto()
    elif opcao == "7":
        atualizarCotacao()
    elif opcao == "8":
        sair()

def main():
    loginUsuario()

main()
