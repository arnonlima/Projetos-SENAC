def cadastrar_produto(estoque):
    print('Cadastrar Produto')
    codigo = input('Código: ').strip()
    if not codigo:
        print('Erro: código inválido.')
        return
    if any(p['código'] == codigo for p in estoque):
        print('Erro: código já cadastrado.')
        return

    nome = input('Nome: ').strip()
    if not nome:
        print('Erro: nome inválido.')
        return

    try:
        preco = float(input('Preço do Quilo: R$ '))
        quantidade = int(input('Quantidade em Quilo: '))
    except ValueError:
        print('Erro: informe um número válido.')
        return

    if preco < 0:
        print('Erro: preço não pode ser negativo.')
        return
    if quantidade < 0:
        print('Erro: quantidade não pode ser negativa.')
        return

    estoque.append({
        'código': codigo,
        'nome': nome,
        'preço': preco,
        'quantidade': quantidade
    })
    print('Produto cadastrado com sucesso!')


def calcular_total(estoque):
    total = sum(p['quantidade'] for p in estoque)
    print(f'Total de produtos em estoque em quilos: {total}')


def exibir_menu():
    print("MENU")
    print("1. Cadastrar Produto")
    print("2. Calcular o Total de Produtos em Estoque")
    print("3. Sair")


def main():
    estoque = []
    while True:
        exibir_menu()
        opcao = input('Escolha uma opção: ')
        if opcao == '1':
            cadastrar_produto(estoque)
        elif opcao == '2':
            calcular_total(estoque)
        elif opcao == '3':
            print('Encerrando...')
            break
        else:
            print("Opção inválida.")


main()
