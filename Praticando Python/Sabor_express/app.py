import os

restaurantes = [{"Nome":"Dona Dé", "Categoria":"Japones", "Ativo":False}, {"Nome":"Doutor Café", "Categoria":"Cafeteria", "Ativo":False}, {"Nome":"Redonda", "Categoria":"Pizzaria", "Ativo":False}]

def exibir_nome_do_programa():
    print("𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤 \n")

def cadastrar_novo_restaurante():
    exibir_submenu("Cadastro de novos Restaurantes")
    nome_restaurante = input("Digite o nome do restaurante para Cadastrar: ")
    categoria = input(f"Digite o nome da Categoria para o restaurante {nome_restaurante}: ")
    dados_restaurante = {"Nome":nome_restaurante, "Categoria":categoria, "Ativo":False}
    restaurantes.append(dados_restaurante)
    print(f"O restaurante {nome_restaurante} foi cadastrado com sucesso!\n")
    voltar_menu_principal()

def listar_restaurantes():
    exibir_submenu("Listando restaurantes")

    print(f"{"Nome do Restaurante".ljust(16)} | {"Categoria".ljust(16)} | {"Status".ljust(16)}\n")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["Nome"]
        categoria = restaurante["Categoria"]
        ativo = "Ativado" if restaurante["Ativo"] else "Desativado"
        print(f"-> {nome_restaurante.ljust(16)} | {categoria.ljust(16)} | {ativo.ljust(16)}")
        '''poderia ser feito assim também
        ativo = restaurante["Ativo"]
        if ativo == False:
            ativo_2 = "Inativo"
        else:
            ativo_2 = "Ativo"
        print(f"-> {nome_restaurante} | {categoria} | {ativo_2}")
        '''
        #print("-> " + restaurante) #poderia ser assim tbm
    voltar_menu_principal()

def alternar_estado_restaurante():
    exibir_submenu("Alterar estado do Restaurante")
    nome_restaurante = input("Digite o nome do restaurante para alterar o estado: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["Nome"]:
            restaurante_encontrado = True
            restaurante["Ativo"] = not restaurante["Ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante["Ativo"] else f"O restaurante { nome_restaurante} foi desativado com sucesso"
            print(mensagem)
            voltar_menu_principal()
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado\n")
        voltar_menu_principal()

def exibir_opcoes():
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurantes")
    print("3. Ativar ou Desativar Restaurante")
    print("4. Sair\n")

def finalizar_app():
    exibir_submenu("Programa Encerrado")

def voltar_menu_principal():
    input("\nDigite qualquer tecla para voltar ao menu principal: ")
    main()

def exibir_submenu(texto):
    os.system("clear")
    #os.system("cls") se for no windows
    firula = "*" * (len(texto))
    print(firula)
    print(texto)
    print(firula)
    print("\n")

def opcao_invalida():
    os.system("clear")
    print("Opção Inválida!\n")
    voltar_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        #print(f"Você escolheu a opção {opcao_escolhida}")

        if opcao_escolhida == 1:
            #print("Cadastrar Restaurante\n")
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            #print("Listar Restaurantes\n")
            #print(restaurantes)
            listar_restaurantes()
        elif opcao_escolhida == 3:
            #print("Ativar Restaurante\n")
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
    """poderiamos utilizar o Match/Case famoso Switch/Case
    opcao_escolhida = int(input('Escolha uma opção: '))
    match opcao_escolhida:
        case 1:
            print('Adicionar restaurante')
        case 2:
            print('Listar restaurantes')
        case 3:
            print('Ativar restaurante')
        case 4:
            print('Finalizar app')
        case _:
            print('Opção inválida!')
    """

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()