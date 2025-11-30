import json

livros = []
jogos = []

def salvar_dados():
    with open("acervo.json", "w", encoding="utf-8") as arquivo:
        json.dump({"livros": livros, "jogos": jogos}, arquivo, ensure_ascii=False, indent=4)


def carregar_dados():
    global livros, jogos
    try:
        with open("acervo.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            livros = dados.get("livros", [])
            jogos = dados.get("jogos", [])
    except FileNotFoundError:
        livros = []
        jogos = []

def menu_principal():
    carregar_dados()

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
            salvar_dados()
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
        print("3. Buscar Jogos")
        print("4. Editar Jogos")
        print("5. Remover Jogo")
        print("6. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_jogo()
        elif opcao == "2":
            listar_jogo()
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
    while True:    
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

        print("1.Adicionar outro livro")    
        print("2.Voltar")
    
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            salvar_dados()
            continue
        elif opcao == "2":
            salvar_dados()
            break
        else:
            print("Opção Inválida!")
            opcao = input("Escolha uma opção: ")

def listar_livro():
    while True:
        print("Lista de Livros")
        
        if not livros :
            print("\n Nenhum livro cadastrado")
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
            continue
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
                salvar_dados()
            else:
                print("Numero inválido!")

            print("1.Editar outro livro")    
            print("2.Voltar")

            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                continue
            elif opcao == "2":
                break
            else:
                print("Opção Inválida!")
                opcao = input("Escolha uma opção: ")
                                   
        except ValueError:
            print("Digite um número válido!")
            editar_livro()
                    

def remover_livro():
    while True:
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
                salvar_dados()

            print("1.Remover outro Livro")    
            print("2.Voltar")
    
            opcao = input("Escolha uma opção: ").strip()
            if opcao == "1":
                salvar_dados()
                continue
            elif opcao == "2":
                salvar_dados()
                break
            else:
                print("Opção Inválida!")
                opcao = input("Escolha uma opção: ")
                     
        except ValueError:
            print("Por favor, digite um número válido.")
            continue


#jogos

def adicionar_jogo():
    while True:    
        print ("Adicionar Jogo")
        titulo = input("\nTitulo: ").strip()
        autor = input("Autor: ").strip()
        genero = input("Gênero: ").strip()
        ano = input("Ano de Lançamento: ").strip()

        jogo = {
            "titulo" : titulo,
            "autor" : autor,
            "genero" : genero,
            "ano" : ano,
        }

        jogos.append(jogo)
        print(f"Jogo '{titulo}' adicionado com sucesso!")

        print("1.Adicionar outro jogo")    
        print("2.Voltar")
    
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            salvar_dados()
            continue
        elif opcao == "2":
            salvar_dados()
            break
        else:
            print("Opção Inválida!")
            opcao = input("Escolha uma opção: ")




def listar_jogo():
     while True:
        print("Lista de Jogos")
        
        if not jogos :
            print("\n Nenhum jogo cadastrado")
        else:
            for i, jogo in enumerate (jogos, start = 1):
                print (f"{i} {jogo['titulo']}, {jogo['autor']}, {jogo['ano']}, {jogo['genero']}")
            
        print("1. Voltar")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            break
        else:
            opcao = input("Escolha uma opção: ")

def listar_del2():
    print("Lista de Jogos")
        
    if not jogos :
        print("\n Nenhum jogo cadastrado")
        print("1. Voltar")
    else:
        for i, jogo in enumerate (jogos, start = 1):
            print (f"{i} {jogo['titulo']}, {jogo['autor']}, {jogo['ano']}, {jogo['genero']}")

def buscar_jogo():
     while True:
        
        print("Buscar Jogo")
        if not jogos:
            print ("Nenhum jogo cadastrado!")
            return
        
        busca = input("Digite o nome ou autor do jogo: ").strip().lower()
        encontrados = []
        
        for jogo in jogos:
            if busca in jogo ['titulo'].lower():
                encontrados.append(jogo)
            elif busca in jogo ['autor'].lower():
                encontrados.append(jogo)
            
        if encontrados:
            print("Jogos encotrados")
            for i, jogo in enumerate (encontrados, start = 1):
                print(f"{i} {jogo['titulo']}, {jogo['autor']}, {jogo['ano']}, {jogo['genero']}") 
                print("\n1. Pesquisar novamente")
                print("2. Voltar")
        else:
            print("\nNenhum jogo encontrado!") 
            print("\n1. Pesquisar novamente")
            print("2. Voltar")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            buscar_jogo()
        elif opcao == "2":
            break
        else:
            opcao = input("Escolha uma opção: ")

def editar_jogo():
    while True:
        
        print("Editar Jogo")
        if not jogos:
            print ("Nenhum livro cadastrado!")
            return
        
        listar_del2()
        try:
            indice = int(input("Digite o numero do Jogo que quer editar: "))
            if indice >= 1:
                jogo = jogos[indice - 1]

                print ("Digite os novos valores")
                print ("Deixe em branco se quiser manter como está")
                novo_titulo = input("Titulo:" ).strip()
                novo_autor = input("Autor: ").strip()
                novo_genero = input("Gênero: ").strip()
                novo_ano = input ("Ano: ").strip()

                if novo_titulo:
                    jogo['titulo'] = novo_titulo
                if novo_autor:
                    jogo['autor'] = novo_autor
                if novo_genero:
                    jogo['genero'] = novo_genero
                if novo_ano:
                    jogo['ano'] = novo_ano

                print("Jogo editado com sucesso!")
                salvar_dados()
            else:
                print("Numero inválido!")

            print("1.Editar outro jogo")    
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
            editar_jogo()

def remover_jogo():
    while True:
        print("Remover Jogo")
        if not jogos:
            print ("Nenhum jogo cadastrado!")
            return
        
        listar_del2()
        try:
            indice = int(input("Digite o numero do livro que quer remover: "))
            if indice >= 1:
                del jogos [indice - 1]
                print ("Jogo removido com sucesso!")
                salvar_dados()

            print("1.Remover outro jogo")    
            print("2.Voltar")
    
            opcao = input("Escolha uma opção: ").strip()
            if opcao == "1":
                salvar_dados()
                continue
            elif opcao == "2":
                salvar_dados()
                break
            else:
                print("Opção Inválida!")
                opcao = input("Escolha uma opção: ")
               
        except ValueError:
            print("Por favor, digite um número válido.")
            continue







menu_principal()