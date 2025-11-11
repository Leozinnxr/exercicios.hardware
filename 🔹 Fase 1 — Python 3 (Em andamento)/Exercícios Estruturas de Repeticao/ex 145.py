cardapio = {
    101: 3.00,
    201: 5.00,
    202: 6.00,
    301: 4.00,
    302: 5.00,
    500: 2.00
}

n = int(input("Quantas pessoas farão o pedido? "))
total = 0

for i in range(1, n + 1):
    print(f"\nPedido da pessoa n°{i}:")
    codigo = int(input("Código do item: "))
    quantidade = int(input("Quantidade: "))
    if codigo in cardapio:
        total += cardapio[codigo] * quantidade
    else:
        print("Código inválido.")

print(f"\nValor total a ser pago: R${total:.2f}")
