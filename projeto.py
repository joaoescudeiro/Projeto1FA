CPF = None # definindo variável CPF
senha = None # definindo variável nome

def cadastroUsuario():
    CPF = input("Digite o seu CPF: ") # solicita o cpf ao usuário

    while True: # executa enquanto o usuario nao digitar uma senha de 6 digitos
        senha = input("Digite a sua senha: ") # solicita uma senha ao usuário

        if len(senha) == 6 and senha.isdigit(): # verifica se a senha contém 6 dígitos com o len() e se são numeros com o isdigit()
            break # sai do loop se a condicao acima for verdadeira
        else: # se a condicao for falsa executa
            print("A senha deve conter 6 números. Digite novamente.") # exibe mensagem dizendo que a senha deve conter 6 numeros

    nome = input("Digite o seu nome: ") # solicita o nome ao usuário
    bd = open("bd.txt","a") # abre o arquivo .txt que possui os dados dos usuários
    bd.write(f"{CPF},{nome},{senha}\n") # faz o registro dos dados digitados no arquivo .txt
    print("Cadastrado") # exibe mensagem de cadastro efetuado

def loginUsuario():
    CPF = input("Digite o seu CPF: ") # solicita o cpf ao usuário
    senha = input("Digite a sua senha: ") # solicita a senha ao usuário
    bd = open("bd.txt") # abre o arquivo .txt que possui os dados dos usuários

    try: # tenta executar o código sem erros (se houver erro ele executa o except)
        for linha in bd: # itera cada linha do arquivo bd.txt aberto anteriormente com o open()
            CPFbd, nome, senhabd = linha.strip().split(',') # descompacta a lista de dados em variáveis individuais
            
            if CPF == CPFbd and senha == senhabd: # verifica se o CPF e a senha estão corretos
                print(f"Olá, {nome}!") # exibe mensagem de olá ao usuário 
                menuGeral() # chama a função do menu pós login 
                return # encerra a execução função
        print("CPF ou senha incorretos.") # exibe mensagem de CPF ou senha incorretos caso a condição de cima for falsa

    except FileNotFoundError: # se o arquivo de dados dos usuários não for encontrado
        print("O arquivo de registros não foi encontrado.") # exibe mensagem de arquivo não encontrado


def consultarSaldo():
    pass

def consultarExtrato():
    pass

def depositar():
    pass

def sacar():
    pass

def comprarCripto():
    pass

def venderCripto():
    pass

def atualizarCotacao():
    pass

def sair():
    exit

def menuGeral():
    opcoes = { # criando dicionário com as opcoes
         "1.":"Consultar saldo",
         "2.":"Consultar extrato",
         "3.":"Depositar",
         "4.":"Sacar",
         "5.":"Comprar criptomoedas",
         "6.":"Vender criptomoedas",
         "7.":"Atualizar cotação",
         "8.":"Sair", # definindo chaves(numero da opcao) e valores(opcao) das opcoes no dicionario
    }

    for numero, opcao in opcoes.items(): # loop para percorrer os pares de chave e valor do dicionario opcoes
        print(f"{numero} {opcao}") # imprime o numero da opcao e a opcao

    opcao = input() # recebe o numero da opcao desejada pelo usuario

    if opcao == 1: # se opcao for 1 executa a funcao consultarSaldo()
        consultarSaldo()
    elif opcao == 2: # se opcao for 2 executa a funcao consultarExtrato()
        consultarExtrato()
    elif opcao == 3: # se opcao for 3 executa a funcao depositar()
        depositar()
    elif opcao == 4: # se opcao for 4 executa a funcao sacar()
        sacar()
    elif opcao == 5: # se opcao for 5 executa a funcao comprarCripto()
        comprarCripto()
    elif opcao == 6: # se opcao for 6 executa a funcao venderCripto()
        venderCripto()
    elif opcao == 7: # se opcao for 7 executa a funcao atualizarCotacao()
        atualizarCotacao()
    elif opcao == 8: # se opcao for 8 executa a funcao sair() que finaliza a execucao do programa
        sair()


def main():
    loginUsuario()

main()