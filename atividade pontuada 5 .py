# biblioteca.py
import os
import time


def exibir_menu():
    
    """Exibe o menu principal do sistema da biblioteca."""
    print("\n--- Sistema de Gestão de Biblioteca ---\n")
    print("1. Cadastrar Livro")
    print("2. Listar Livros")
    print("3. Buscar Livro por Título")
    print("4. Emprestar/Devolver Livro")
    print("0. Sair")
    print("---------------------------------------")

def cadastrar_livro(lista_livros: list):
 
    print("\n=== Cadastrar Novo Livro ===")
    titulo = input("Título do novo livro: ").strip()
    autor = input("Autor do livro: ").strip()

    while True: # Loop para garantir entrada válida de preço
        try:
            preco = float(input("Preço do livro: "))
            if preco < 0:
                print("Preço não pode ser negativo. Tente novamente.")
                time.sleep(2.5)
            else:
                break
        except ValueError:
            print("Entrada inválida para o preço. Por favor, digite um número.")
            
        time.sleep(2.5)


    while True: 
        try:
            quantidade = int(input("Quantidade em estoque: "))
            if quantidade < 0:
                print("Quantidade não pode ser negativa. Tente novamente.")
            else:
                break
        except ValueError:
            print("Entrada inválida para a quantidade. Por favor, digite um número inteiro.")
    
    # um campo 'emprestados' para controlar quantos estão fora
    livro = {'titulo': titulo, 'autor': autor, 'preco': preco, 'quantidade': quantidade, 'emprestados': 0}
    lista_livros.append(livro)
    print(f"Livro '{titulo}' cadastrado com sucesso!")
    time.sleep(4)


def listar_livros(lista_livros: list):

    print("\n--- Livros Cadastrados ---")
    if not lista_livros:
        print("Nenhum livro cadastrado ainda.")
        time.sleep(2.5)

        return

    for i, livro in enumerate(lista_livros):
        disponivel = livro['quantidade'] - livro['emprestados']
        print(f"ID: {i+1} | Título: {livro['titulo']} | Autor: {livro['autor']} | "
              f"Preço: R${livro['preco']:.2f} | Total: {livro['quantidade']} | "
              f"Disponível: {disponivel} | Emprestados: {livro['emprestados']}")
        print("-" * 60) # Separador para melhor legibilidade
        
        time.sleep(5)

def buscar_livro(lista_livros: list):
    """
    Busca um livro por título e exibe suas informações.
    """
    print("\n=== Buscar Livro ===")
    if not lista_livros:
        print("Nenhum livro cadastrado para buscar.")
        return

    termo_busca = input("Digite o título do livro que deseja buscar: ").strip().lower()
    encontrados = []
    for livro in lista_livros:
        if termo_busca in livro['titulo'].lower():
            encontrados.append(livro)
    
    if not encontrados:
        print(f"Nenhum livro encontrado com o título '{termo_busca}'.")
    else:
        print("\n--- Livros Encontrados ---")
        for i, livro in enumerate(encontrados):
            disponivel = livro['quantidade'] - livro['emprestados']
            print(f"ID: {i+1} | Título: {livro['titulo']} | Autor: {livro['autor']} | "
                  f"Preço: R${livro['preco']:.2f} | Total: {livro['quantidade']} | "
                  f"Disponível: {disponivel} | Emprestados: {livro['emprestados']}")
            print("-" * 60)

    time.sleep(2.5)

def emprestar_devolver_livro(lista_livros: list):
    """
    Permite emprestar ou devolver um livro, atualizando sua quantidade.
    """
    print("\n=== Emprestar/Devolver Livro ===")
    if not lista_livros:
        print("Nenhum livro cadastrado para emprestar/devolver.")
        return

    listar_livros(lista_livros) 

    livro_selecionado = None
    while livro_selecionado is None:
        try:
            id_livro = int(input("Digite o ID do livro (para emprestar/devolver): ")) - 1
            if 0 <= id_livro < len(lista_livros):
                livro_selecionado = lista_livros[id_livro]
            else:
                print("ID de livro inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida para o ID. Por favor, digite um número inteiro.")

    print(f"\nLivro selecionado: {livro_selecionado['titulo']}")
    print("1. Emprestar")
    print("2. Devolver")
    print("0. Cancelar")

    while True:
        try:
            acao = int(input("Escolha a ação (1-Emprestar, 2-Devolver, 0-Cancelar): "))
            if acao in [0, 1, 2]:
                break
            else:
                print("Opção inválida. Escolha 1, 2 ou 0.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    if acao == 0:
        print("Operação cancelada.")
        return

    while True:
        try:
            quantidade_operacao = int(input("Quantidade: "))
            if quantidade_operacao <= 0:
                print("A quantidade deve ser positiva.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")


    if acao == 1: # Emprestar
        if livro_selecionado['quantidade'] - livro_selecionado['emprestados'] >= quantidade_operacao:
            livro_selecionado['emprestados'] += quantidade_operacao
            print(f"{quantidade_operacao} cópia(s) de '{livro_selecionado['titulo']}' emprestada(s) com sucesso!")
        else:
            print(f"Quantidade insuficiente disponível. Restam {livro_selecionado['quantidade'] - livro_selecionado['emprestados']} cópias.")
    elif acao == 2: # Devolver
        if livro_selecionado['emprestados'] >= quantidade_operacao:
            livro_selecionado['emprestados'] -= quantidade_operacao
            print(f"{quantidade_operacao} cópia(s) de '{livro_selecionado['titulo']}' devolvida(s) com sucesso!")
        else:
            print(f"Não há {quantidade_operacao} cópias emprestadas para devolver. Atualmente {livro_selecionado['emprestados']} emprestadas.")

    time.sleep(2.5)

def main():
    """Função principal que gerencia o fluxo do sistema da biblioteca."""
    lista_livros = []

    while True:

        os.system("cls || clear")

        exibir_menu()

        escolha = int(input("Escolha uma opção: "))
        os.system("cls || clear")

        match escolha:
            case 1:
                cadastrar_livro(lista_livros)
            case 2:
                listar_livros(lista_livros)
            case 3:
                buscar_livro(lista_livros)
            case 4:
                emprestar_devolver_livro(lista_livros)
            case 0:
                print("Saindo do sistema. Até mais!")
                break

            case _: # Padrão curinga para qualquer outra entrada
                print("Opção inválida. Por favor, escolha uma opção de 0 a 4.")

if __name__ == "__main__":
    main()