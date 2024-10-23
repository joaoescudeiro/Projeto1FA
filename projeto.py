import datetime

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
    usuario = usuariologado["CPF"]

    if senha != usuariologado["senha"]:
        print("Senha incorreta. Tente novamente.")
        return
    
    bd = open("bd.txt", "r")
    for linha in bd:
        CPFbd, nome, senhabd, reais, bitcoin, ethereum, ripple = linha.strip().split(",")

        if senha == senhabd and usuario == CPFbd:
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
    senha = input("Digite a sua senha: ")

    if senha != usuariologado["senha"]:
        print("Senha incorreta. Tente novamente.")
        return

    usuario = usuariologado["CPF"]
    extrato = []

    with open("bd.txt", "r") as bd:
        for linha in bd:
            CPFbd, nome, senhabd, reais, bitcoin, ethereum, ripple = linha.strip().split(",")
            if CPFbd == usuario:
                print(f"Nome: {nome}")
                print(f"CPF: {CPFbd}")
                with open(f"extrato_{CPFbd}.txt", "r") as arq_extrato:
                    extrato = arq_extrato.readlines()
                    for linha_extrato in extrato:
                        print(linha_extrato.strip())
                return
    print("Extrato não encontrado.")





def depositar():
    senha = input("Digite a sua senha: ")

    if senha != usuariologado["senha"]:
        print("Senha incorreta. Tente novamente.")
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

                data = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
                tipotransacao = "+"
                cotacao = 0.0
                taxa = 0.00

                # cria ou atualiza o arquivo de extrato
                with open(f"extrato_{CPFbd}.txt", "a") as extrato:
                    extrato.write(f"{data} {tipotransacao} {valordeposito:.2f} REAL "
                                  f"CT: {cotacao:.2f} TX: {taxa:.2f} REAL: {novosaldoreais:.2f} "
                                  f"BTC: {float(bitcoin):.4f} ETH: {float(ethereum):.2f} XRP: {float(ripple):.2f}\n")
            else:
                bd.write(linha) # reescreve o registro dos outros usuários





def sacar():
    senha = input("Digite a sua senha: ")

    if senha != usuariologado["senha"]:
        print("Senha incorreta. Tente novamente.")
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
                    exit
                    
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

                    datahora = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
                    tipotransacao = "-"
                    cotacao = 0.0
                    taxa = 0.00

                    # cria ou atualiza o arquivo de extrato
                    with open(f"extrato_{CPFbd}.txt", "a") as extrato:
                        extrato.write(f"{datahora} {tipotransacao} {valorsaque:.2f} REAL "
                                      f"CT: {cotacao:.2f} TX: {taxa:.2f} REAL: {novosaldo:.2f} "
                                      f"BTC: {float(bitcoin):.4f} ETH: {float(ethereum):.2f} XRP: {float(ripple):.2f}\n")
            else:
                bd.write(linha) # reescreve o registro dos outros usuários





def comprarCripto():
    senha = input("Digite a sua senha: ")

    if senha != usuariologado["senha"]:
        print("Senha incorreta. Tente novamente.")
        return

    cotacao_btc = 377767.29
    cotacao_eth = 14279.99
    cotacao_xrp = 2.99

    print(f"Cotações:\nBTC: {cotacao_btc} REAL\nETH: {cotacao_eth} REAL\nXRP: {cotacao_xrp} REAL")

    cripto = input("Qual criptomoeda deseja comprar? (BTC/ETH/XRP): ").upper()
    if cripto not in ["BTC", "ETH", "XRP"]:
        print("Cripto digitado não existe.")
        return

    valor_compra = float(input("Digite o valor em reais que deseja usar na compra: "))
    
    taxa = 0.02  # 2% de taxa de compra
    valor_final = valor_compra - (valor_compra * taxa)

    with open("bd.txt", "r") as bd:
        linhas = bd.readlines()

    with open("bd.txt", "w") as bd:
        for linha in linhas:
            CPFbd, nome, senhabd, reais, bitcoin, ethereum, ripple = linha.strip().split(",")

            if CPFbd == usuariologado["CPF"]:
                saldo = float(reais)

                if saldo < valor_compra:
                    print(f"Saldo insuficiente. Saldo atual: {saldo:.2f}")
                    for linha in linhas:
                        bd.write(linha)
                    return
                
                # atualiza saldo e criptomoeda
                novosaldo = saldo - valor_compra
                if cripto == "BTC":
                    bitcoin = float(bitcoin) + (valor_final / cotacao_btc)
                elif cripto == "ETH":
                    ethereum = float(ethereum) + (valor_final / cotacao_eth)
                elif cripto == "XRP":
                    ripple = float(ripple) + (valor_final / cotacao_xrp)

                bd.write(f"{CPFbd},{nome},{senhabd},{novosaldo},{bitcoin},{ethereum},{ripple}\n")
                print(f"Compra realizada com sucesso. Taxa aplicada: {taxa * 100}%")
                print(f"Seu saldo atualizado:")
                print(f"Nome: {nome}")
                print(f"CPF: {CPFbd}")
                print(f"Reais: {float(novosaldo):.2f}")
                print(f"Bitcoin: {float(bitcoin):.4f}")
                print(f"Ethereum: {float(ethereum):.2f}")
                print(f"Ripple: {float(ripple):.2f}")

                # registro no extrato
                datahora = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
                tipotransacao = "+"  # compra de cripto é uma transação positiva
                cotacao = 0.0

                if cripto == "BTC":
                    cotacao = cotacao_btc
                elif cripto == "ETH":
                    cotacao = cotacao_eth
                elif cripto == "XRP":
                    cotacao = cotacao_xrp

                # cria ou atualiza o arquivo de extrato
                with open(f"extrato_{CPFbd}.txt", "a") as extrato:
                    extrato.write(f"{datahora} {tipotransacao} {valor_compra:.2f} {cripto} "
                                  f"CT: {cotacao:.2f} TX: {taxa:.2f} REAL: {novosaldo:.2f} "
                                  f"BTC: {float(bitcoin):.4f} ETH: {float(ethereum):.2f} XRP: {float(ripple):.2f}\n")
            else:
                bd.write(linha)





def venderCripto():
    senha = input("Digite a sua senha: ")

    if senha != usuariologado["senha"]:
        print("Senha incorreta. Tente novamente.")
        return

    cotacao_btc = 377767.29
    cotacao_eth = 14279.99
    cotacao_xrp = 2.99

    print(f"Cotações:\nBTC: {cotacao_btc} REAL\nETH: {cotacao_eth} REAL\nXRP: {cotacao_xrp} REAL")

    cripto = input("Qual criptomoeda deseja vender? (BTC/ETH/XRP): ").upper()
    if cripto not in ["BTC", "ETH", "XRP"]:
        print("Cripto digitado não existe.")
        return

    valor_venda = float(input("Digite o valor em reais que deseja vender: "))
    
    taxa = 0.02  # 2% de taxa de venda
    valor_final = valor_venda - (valor_venda * taxa)

    with open("bd.txt", "r") as bd:
        linhas = bd.readlines()

    with open("bd.txt", "w") as bd:
        for linha in linhas:
            CPFbd, nome, senhabd, reais, bitcoin, ethereum, ripple = linha.strip().split(",")

            if CPFbd == usuariologado["CPF"]:
                if cripto == "BTC" and float(bitcoin) * cotacao_btc < valor_venda:
                    print("Saldo insuficiente em BTC.")
                    for linha in linhas:
                        bd.write(linha)
                    return
                elif cripto == "ETH" and float(ethereum) * cotacao_eth < valor_venda:
                    print("Saldo insuficiente em ETH.")
                    for linha in linhas:
                        bd.write(linha)
                    return
                elif cripto == "XRP" and float(ripple) * cotacao_xrp < valor_venda:
                    print("Saldo insuficiente em XRP.")
                    for linha in linhas:
                        bd.write(linha)
                    return

                # atualiza saldo e criptomoeda
                novosaldo = float(reais) + valor_final
                if cripto == "BTC":
                    bitcoin = float(bitcoin) - (valor_venda / cotacao_btc)
                elif cripto == "ETH":
                    ethereum = float(ethereum) - (valor_venda / cotacao_eth)
                elif cripto == "XRP":
                    ripple = float(ripple) - (valor_venda / cotacao_xrp)

                bd.write(f"{CPFbd},{nome},{senhabd},{novosaldo},{bitcoin},{ethereum},{ripple}\n")
                print(f"Venda realizada com sucesso! Taxa aplicada: {taxa * 100}%")
                print(f"Seu saldo atualizado:")
                print(f"Nome: {nome}")
                print(f"CPF: {CPFbd}")
                print(f"Reais: {float(novosaldo):.2f}")
                print(f"Bitcoin: {float(bitcoin):.4f}")
                print(f"Ethereum: {float(ethereum):.2f}")
                print(f"Ripple: {float(ripple):.2f}")

                # registro no extrato
                datahora = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
                tipotransacao = "-"  # venda é uma transação negativa

                if cripto == "BTC":
                    cotacao = cotacao_btc
                elif cripto == "ETH":
                    cotacao = cotacao_eth
                elif cripto == "XRP":
                    cotacao = cotacao_xrp

                # cria ou atualiza o arquivo de extrato
                with open(f"extrato_{CPFbd}.txt", "a") as extrato:
                    extrato.write(f"{datahora} {tipotransacao} {valor_venda:.2f} {cripto} "
                                  f"CT: {cotacao:.2f} TX: {taxa:.2f} REAL: {novosaldo:.2f} "
                                  f"BTC: {float(bitcoin):.4f} ETH: {float(ethereum):.2f} XRP: {float(ripple):.2f}\n")
            else:
                bd.write(linha)





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
    else:
        print("Número digitado não pertence a nenhuma opção.")
        return

def main():
    loginUsuario()
    # cadastroUsuario()
main()
