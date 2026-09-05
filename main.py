import time

def pausar():
    print("\nVoltando ao menu...")
    time.sleep(3)

usuarios = [
    {
        "nome": "Lucas",
        "idade": 18,
        "cidade": "São Paulo"
    },
    {
        "nome": "João",
        "idade": 16,
        "cidade": "Guarulhos"
    }
]

def listar_usuarios(usuarios):
    for usuario in usuarios:
        print(f"\n{usuario['nome']} - {usuario['idade']} - {usuario['cidade']}")

def buscar_usuario(usuarios):
    encontrado = False
    nome_usuario = input("\nDigite o nome do usuário: ").upper()

    for usuario in usuarios:
        if nome_usuario == usuario['nome'].upper():
            encontrado = True

            print("Usuário encontrado!")

            print(f"\nNome: {usuario['nome']}")
            print(f"\nIdade: {usuario['idade']}")
            print(f"\nCidade: {usuario['cidade']}")
            return

    if not encontrado:
        print("Usuário não encontrado.")

def cadastrar_usuario(usuarios):
    add_usuario = input("\nDigite o nome: ").upper()

    for usuario in usuarios: 
        if add_usuario == usuario["nome"].upper():
            print("\nError! Esse usuário já está cadastrado.") 
            return

    while True:
        try:
            add_idade = int(input("\nDigite a idade: "))

            if add_idade < 0 or add_idade > 120: 
                print("Error! Digite uma idade entre 0 e 120 anos.") 
                continue
            break

        except ValueError:
            print("Error! Digite uma idade válida usando apenas números.")

    add_cidade = input("\nDigite a cidade: ").upper()

    usuarios.append({
        "nome": add_usuario,
        "idade": add_idade,
        "cidade": add_cidade
    })

    print(f"\nUsuário {add_usuario} cadastrado com sucesso.")
 
def excluir_usuario(usuarios):
    nome_usuario = input("Digite o nome do usuário que deseja excluir: ")

    for usuario in usuarios:
        if nome_usuario.upper() == usuario['nome'].upper():
            usuarios.remove(usuario)
            print(f"Usuário {usuario['nome']} excluído com sucesso!")
            return

    print("Usuário não encontrado.")

def atualizar_usuario(usuarios):

    att_nome = input("Digite o nome do usuário que deseja atualizar: ")

    encontrado = False

    for usuario in usuarios:

        if att_nome.upper() == usuario['nome'].upper():

            encontrado = True

            novo_nome = input("Novo nome: ").upper()

            for outro_usuario in usuarios: 
                if (novo_nome == outro_usuario["nome"].upper() and outro_usuario != usuario ): 
                    print("\nError! Esse nome já está sendo usado por outro usuário.") 
                    return

            while True:
                try:
                    nova_idade = int(input("Nova idade: "))
                    break

                except ValueError:
                    print("Error! Digite uma idade válida usando apenas números.")

            nova_cidade = input("Nova cidade: ").upper()

            usuario["nome"] = novo_nome
            usuario["idade"] = nova_idade
            usuario["cidade"] = nova_cidade

            print("Usuário atualizado com sucesso!")

            return

    if not encontrado:
        print("Usuário não encontrado.")

def sistema_usuarios():
    print("\n========== SISTEMA DE USUÁRIOS ==========")
    print("1 - Listar usuários")
    print("2 - Buscar usuário")
    print("3 - Cadastrar usuário")
    print("4 - Atualizar usuário")
    print("5 - Excluir usuário")
    print("0 - Sair")
    print("==========================================")

while True:

    sistema_usuarios()

    try:
        opcao = int(input("Escolha uma opção: "))

    except ValueError:
        print("\nError! Digite apenas números!")
        time.sleep(2)
        continue

    if opcao == 1:
        listar_usuarios(usuarios)
        pausar()

    elif opcao == 2:
        buscar_usuario(usuarios)
        pausar()

    elif opcao == 3:
        cadastrar_usuario(usuarios)
        pausar()

    elif opcao == 4:
        atualizar_usuario(usuarios)
        pausar()

    elif opcao == 5:
        excluir_usuario(usuarios)
        pausar()

    elif opcao == 0:
        print("Programa encerrado.")
        break

    else:
        print("Opção não encontrada.")
        pausar()
