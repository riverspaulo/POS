# Código base 
    # import requests

    # if __name__ == "__main__":
    #     url = "http://127.0.0.1:8000"
    #     r = requests.get(f"{url}/livros")
    #     print(r.text)
    #     livro = {
    #         "titulo": "Python como Programar",
    #         "ano": 2024,
    #         "edicao": 1
    #     }
    #     r = requests.post(f"{url}/livros",json=livro)
    #     print(r.status_code)
    #     print(r.text)
    #     pesquisa = "Python como Programar"
    #     r = requests.get(f"{url}/livros/{pesquisa}")
    #     print(r.status_code)
    #     print(r.text)
    #     r = requests.delete(f"{url}/livros/{pesquisa}")
    #     print(r.status_code)

import requests

url = "http://127.0.0.1:8000"

def listar_livros():
    r = requests.get(f"{url}/livros")
    if r.status_code == 200:
        livros = r.json()
        if livros:
            for livro in livros:
                print(livro)
        else:
            print("Nenhum livro cadastrado.")
    else:
        print("Erro ao listar livros.")

def pesquisar_livro():
    titulo = input("Digite o título do livro: ")
    r = requests.get(f"{url}/livros/{titulo}")
    if r.status_code == 200:
        print(r.json())
    else:
        print("Livro não encontrado.")

def cadastrar_livro():
    titulo = input("Título: ")
    ano = int(input("Ano: "))
    edicao = int(input("Edição: "))
    livro = {"titulo": titulo, "ano": ano, "edicao": edicao}
    r = requests.post(f"{url}/livros", json=livro)
    if r.status_code == 200:
        print("Livro cadastrado com sucesso.")
    else:
        print("Erro ao cadastrar livro.")

def deletar_livro():
    titulo = input("Digite o título do livro a ser deletado: ")
    r = requests.delete(f"{url}/livros/{titulo}")
    if r.status_code == 200:
        print("Livro deletado com sucesso.")
    else:
        print("Livro não encontrado.")

def editar_livro():
    titulo = input("Digite o título do livro a ser editado: ")
    r = requests.get(f"{url}/livros/{titulo}")
    if r.status_code == 200:
        livro_antigo = r.json()
        print("Digite os novos dados (deixe em branco para manter o valor atual):")
        novo_titulo = input(f"Título [{livro_antigo['titulo']}]: ") or livro_antigo['titulo']
        novo_ano = input(f"Ano [{livro_antigo['ano']}]: ") or livro_antigo['ano']
        nova_edicao = input(f"Edição [{livro_antigo['edicao']}]: ") or livro_antigo['edicao']

        livro_editado = {
            "titulo": novo_titulo,
            "ano": int(novo_ano),
            "edicao": int(nova_edicao)
        }

        r = requests.put(f"{url}/livros/{titulo}", json=livro_editado)
        if r.status_code == 200:
            print("Livro editado com sucesso.")
        else:
            print("Erro ao editar livro.")
    else:
        print("Livro não encontrado.")


if __name__ == "__main__":
    while True:
        print("-----------Menu-----------")
        print("1 - Listar todos os livros")
        print("2 - Pesquisar livro por título")
        print("3 - Cadastrar um livro")
        print("4 - Deletar um livro")
        print("5 - Editar um livro")
        print("6 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_livros()
        elif opcao == "2":
            pesquisar_livro()
        elif opcao == "3":
            cadastrar_livro()
        elif opcao == "4":
            deletar_livro()
        elif opcao == "5":
            editar_livro()
        elif opcao == "6":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida.")
