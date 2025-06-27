# pip install requests

import requests
URL= "http://127.0.0.1:8000"

def listar_livros():
    r = requests.get(f"{URL}/livros")
    if r.status_code == 200:
        print(r.text)

def cadastrar_livros():
    titulo = input("Digite o título: ")
    ano = int(input("Digite o ano: "))
    edicao = int(input("Digite a edicao: "))
    livro = {
        "titulo":titulo,
        "ano":ano,
        "edicao":edicao
    }
    r = requests.post(f"{URL}/livros", json=livro)
def listar_livro(titulo):
    r = requests.get(f"{URL}/livros/{titulo}")
    if r.status_code == 200:
        print(r.text)

def excluir_livros(titulo):
    pass

def menu():
    print ("1 - Listar Livros")
    print ("2 - Listar Livros pelo título")
    print ("3 - Cadastrar Livros")
    print ("4 - Deletar Livros")
    print ("5 - Sair ")
    print ("--------------------------")
    return int(input("Digite sua opção:"))
opcao = menu()
while opcao != 5:
    if opcao == 1:
        listar_livros()
        print ("--------------------------")
    elif opcao == 2:
        titulo = input("Digite o título:")
        listar_livros(titulo)
    elif opcao == 3:
        cadastrar_livros()
        print ("--------------------------")
    elif opcao == 4:
        titulo = input("Digite o livro:")
        excluir_livros(titulo)
    opcao = menu()


