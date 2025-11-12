livros = []
jogos = []

def menu_principal():
    while True:
        print("Menu")
        print ("\n1. Livros")
        print ("2. Jogos")
        print ("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_livros()
        elif opcao == "2":
            menu_jogos()
        elif opcao == "3":
            print ("Encerrando programa")
            break
        else:
            print("Opção inválida! Digite Novamente")

def menu_livros():
    while True:    
        print("Biblioteca de Livros")
        print("\n1. Adicionar Livro")
        print("2. Listar livros")
        print("3. Buscar Livro")
        print("4. Editar Livro")
        print("5. Remover Livro")
        print("6. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_livro()
        elif opcao == "2":
            listar_livro()
        elif opcao == "3":
            buscar_livro()
        elif opcao == "4":
            editar_livro()
        elif opcao == "5":
            remover_livro()
        elif opcao == "6":
            break
        else:
            print("Opção inválida! Digite Novamente")


def menu_jogos():
    while True:
        print("Biblioteca de Jogos")
        print("\n1. Adicionar Jogo")
        print("2. Listar Jogos")
        print("4. Editar Jogos")
        print("5. Remover Jogo")
        print("6. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_jogo()
        elif opcao == "2":
            listar_jogo
        elif opcao == "3":
            buscar_jogo()
        elif opcao == "4":
            editar_jogo()
        elif opcao == "5":
            remover_jogo()
        elif opcao == "6":
            break
        else:
            print("Opção inválida! Digite Novamente")

        

def adicionar_livro():
    print ("Adicionar Livro")
    titulo = input("\nTitulo: ").strip()
    autor = input("Autor: ").strip()
    genero = input("Gênero: ").strip()
    ano = input("Ano de Lançamento: ").strip()

    livro = {
        "titulo" : titulo,
        "autor" : autor,
        "genero" : genero,
        "ano" : ano,
    }

    livros.append(livro)
    print(f"Livro '{titulo}' adicionado com sucesso!")

def listar_livro():
    while True:
        print("Lista de Livros")
        
        if not livros :
            print("\n Nenhum livro cadastrado")
            print("1. Voltar")
        else:
            for i, livro in enumerate (livros, start = 1):
                print (f"{i} {livro['titulo']}, {livro['autor']}, {livro['ano']}, {livro['genero']}")
            
        print("1. Voltar")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            break
        else:
            opcao = input("Escolha uma opção: ")

def listar_del():
        
        print("Lista de Livros")
        
        if not livros :
            print("\n Nenhum livro cadastrado")
            print("1. Voltar")
        else:
            for i, livro in enumerate (livros, start = 1):
                print (f"{i} {livro['titulo']}, {livro['autor']}, {livro['genero']}, {livro['ano']}")
            

def buscar_livro():
    while True:
        
        print("Buscar Livro")
        if not livros:
            print ("Nenhum livro cadastrado!")
            return
        
        busca = input("Digite o nome ou autor do Livro: ").strip().lower()
        encontrados = []
        
        for livro in livros:
            if busca in livro ['titulo'].lower():
                encontrados.append(livro)
            elif busca in livro ['autor'].lower():
                encontrados.append(livro)
            
        if encontrados:
            print("Livros encotrados")
            for i, livro in enumerate (encontrados, start = 1):
                print(f"{i} {livro['titulo']}, {livro['autor']}, {livro['ano']}, {livro['genero']}") 
                print("\n1. Pesquisar novamente")
                print("2. Voltar")
        else:
            print("\nNenhum livro encontrado!") 
            print("\n1. Pesquisar novamente")
            print("2. Voltar")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            buscar_livro
        elif opcao == "2":
            break
        else:
            opcao = input("Escolha uma opção: ")




def editar_livro():
    while True:
        
        print("Editar Livro")
        if not livros:
            print ("Nenhum livro cadastrado!")
            return
        
        listar_del()
        try:
            indice = int(input("Digite o numero do livro que quer editar: "))
            if indice >= 1:
                livro = livros[indice - 1]

                print ("Digite os novos valores")
                print ("Deixe em branco se quiser manter como está")
                novo_titulo = input("Titulo:" ).strip()
                novo_autor = input("Autor: ").strip()
                novo_genero = input("Gênero: ").strip()
                novo_ano = input ("Ano: ").strip()

                if novo_titulo:
                    livro['titulo'] = novo_titulo
                if novo_autor:
                    livro['autor'] = novo_autor
                if novo_genero:
                    livro['genero'] = novo_genero
                if novo_ano:
                    livro['ano'] = novo_ano

                print("Livro editado com sucesso!")
            else:
                print("Numero inválido!")

            print("1.Editar outro livro")    
            print("2.Voltar")

            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                editar_livro()
            elif opcao == "2":
                break
            else:
                print("Opção Inválida!")
                opcao = input("Escolha uma opção: ")
                                   
        except ValueError:
            print("Digite um número válido!")
            editar_livro()
                    




def remover_livro():

        print("Remover Livro")
        if not livros:
            print ("Nenhum livro cadastrado!")
            return
        
        listar_del()
        try:
            indice = int(input("Digite o numero do livro que quer remover: "))
            if indice >= 1:
                del livros [indice - 1]
                print ("Livro removido com sucesso!")
               
        except ValueError:
            print("Por favor, digite um número válido.")
            remover_livro()




        #busca = input("Digite o titulo do livro: ")
        #encontrados = []

        #for livro in livros:
            #if busca in livros:
                #encontrados.append(livros)

        #if encontrados:
           # for i, livro in enumerate (encontrados,start = 1):
               # print (f"{i} {livro['titulo']}, {livro['autor']}, {livro['ano']},{livro['genero']}")
                


        


#jogos

def adicionar_jogo():
    print("Função: adicionar jogo (a implementar)")

def listar_jogo():
    print("Função: listar jogos (a implementar)")

def buscar_jogo():
    print("Função: buscar jogo (a implementar)")

def editar_jogo():
    print("Função: editar jogo (a implementar)")

def remover_jogo():
    print("Função: remover jogo (a implementar)")






#def adicionar_item():
   # titulo = input("Titulo: ")
   # genero = input("Gênero: ")
   # autor = input("Autor: ")
   # ano = input("Ano de Lançamento: ")

menu_principal()