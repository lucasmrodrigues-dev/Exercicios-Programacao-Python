apagar = 0

while True:
    codigo = int(input("Código da mercadoria (0 para finalizar): "))
    preco = 0

    if codigo == 0:
        break
    elif codigo == 1:
        preco = 0.50
    elif codigo == 2:
        preco = 1.00
    elif codigo == 3:
        preco = 4.00
    elif codigo == 5:
        preco = 7.00
    elif codigo == 9:
        preco = 8.00
    else:
        print("Código inválido!\n")

    # Só solicita a quantidade e acumula o valor se o código digitado for válido
    if preco != 0:
        quantidade = int(input("Quantidade: "))
        apagar = apagar + (preco * quantidade)
        print(f"Subtotal parcial: R$ {apagar:.2f}\n")

print("-" * 30)
print(f"Total a pagar: R$ {apagar:8.2f}")