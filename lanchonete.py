
def pedir_nome():
    nome = input("Informe o seu nome: ")

    while nome == "":
        print("A caixa de nome não pode estar vazia.")
        nome = input("Informe o seu nome: ")

    return nome


def menu_pedidos():
    print("=" * 50)
    print("Bem-vindo à Pythonete")
    print("=" * 50)
    print("PROD       COD       VALOR")
    print("X-bacon     1        16,00")
    print("X-salada    2        14,00")
    print("X-tudo      3        18,00")
    print("Fritas      4        12,00")
    print("Coca        5         6,00")
    print("Suco        6         7,50")
    print("Finalizar   0")

    codigo_produto = int(input("Informe o código: "))

    while codigo_produto < 0 or codigo_produto > 6:
        print("Informe um código válido!")
        codigo_produto = int(input("Informe o código: "))

    return codigo_produto


def produtos_valor(codigo_produto):
    if codigo_produto == 1:
        valor = 16.00
    elif codigo_produto == 2:
        valor = 14.00
    elif codigo_produto == 3:
        valor = 18.00
    elif codigo_produto == 4:
        valor = 12.00
    elif codigo_produto == 5:
        valor = 6.00
    elif codigo_produto == 6:
        valor = 7.50

    return valor


def quantidade(codigo_produto):
    qtd = int(input("Informe a quantidade: "))

    while qtd <= 0:
        print("Informe uma quantidade válida")
        qtd = int(input("Informe a quantidade: "))

    valor = produtos_valor(codigo_produto)
    total = valor * qtd

    return total


def aplicar_desconto(total):
    if total < 50:
        desconto = 0
    elif total < 100:
        desconto = total * 0.05
    else:
        desconto = total * 0.10

    total_final = total - desconto

    return desconto, total_final


def forma_de_pagamento():
    codigop = int(input(
        "Selecione forma de pagamento: "
        "Dinheiro, cartão ou Pix (1, 2 ou 3): "
    ))

    while codigop < 1 or codigop > 3:
        print("Forma de pagamento inválida")
        codigop = int(input(
            "Selecione forma de pagamento: "
            "Dinheiro, cartão ou Pix (1, 2 ou 3): "
        ))

    if codigop == 1:
        pagamento = "Dinheiro"
    elif codigop == 2:
        pagamento = "Cartão"
    else:
        pagamento = "Pix"

    return pagamento


nome = pedir_nome()
total_geral = 0

while True:
    codigo = menu_pedidos()

    if codigo == 0:
        if total_geral == 0:
            print("Voce nao adicionou nenhum produto. Adicione pelo menos um item.")
            continue
        break

    total = quantidade(codigo)
    total_geral = total_geral + total


if total_geral > 0:
    desconto, total_final = aplicar_desconto(total_geral)
    pagamento = forma_de_pagamento()

    if total_geral < 50:
        percentual = 0
    elif total_geral < 100:
        percentual = 5
    else:
        percentual = 10
else:
    desconto = 0
    total_final = 0
    percentual = 0
    pagamento = "Não realizado"

print("=" * 50)
print("           RESUMO DO PEDIDO")
print("=" * 50)
print(f"Nome do cliente:       {nome}")
print("-" * 50)
print(f"Valor original:        R$ {total_geral:.2f}")
print(f"Desconto aplicado:     {percentual}%")
print(f"Valor do desconto:     R$ {desconto:.2f}")
print(f"Valor final:           R$ {total_final:.2f}")
print(f"Forma de pagamento:    {pagamento}")
print("=" * 50)
print("           Pythonete .exit")
print("=" * 50)
