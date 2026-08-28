deposito = float(input("Depósito inicial: R$ "))
taxa = float(input("Taxa de juros mensal (ex: 3 para 3%): "))

mes = 1
saldo = deposito

while mes <= 24:
    saldo = saldo + (saldo * (taxa / 100))
    print(f"Saldo do mês {mes:2d}: R$ {saldo:8.2f}")
    mes = mes + 1

juros_totais = saldo - deposito
print("-" * 35)
print(f"Rendimento total de juros: R$ {juros_totais:8.2f}")
print(f"Saldo final acumulado: R$ {saldo:8.2f}")