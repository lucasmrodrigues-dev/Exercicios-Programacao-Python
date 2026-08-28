consumo = float(input("Consumo em kWh: "))
tipo = input("Tipo da instalação (R - Residencial, C - Comercial, I - Industrial): ").strip().upper()

preco = 0.0

if tipo == "R":
    if consumo <= 500:
        preco = 0.40
    else:
        preco = 0.65
elif tipo == "C":
    if consumo <= 1000:
        preco = 0.55
    else:
        preco = 0.60
elif tipo == "I":
    if consumo <= 5000:
        preco = 0.55
    else:
        preco = 0.60
else:
    print("Erro! Tipo de instalação desconhecido.")

if preco > 0:
    custo = consumo * preco
    print(f"Valor a pagar: R$ {custo:.2f}")