divida = float(input("Dívida inicial: R$ "))
taxa = float(input("Juros mensais (Ex.: 3 para 3%): "))
pagamento = float(input("Pagamento mensal: R$ "))

# Validação: Se os juros do 1º mês forem maiores que o pagamento, a dívida é infinita
if divida * (taxa / 100) >= pagamento:
    print("\nSua dívida nunca será paga, pois os juros são maiores ou iguais ao pagamento mensal!")
else:
    saldo = divida
    total_pago = 0
    total_juros = 0
    mes = 1

    while saldo > 0:
        juros = saldo * (taxa / 100)
        total_juros += juros
        saldo = saldo + juros

        if saldo >= pagamento:
            saldo -= pagamento
            total_pago += pagamento
        else:
            # No último mês, paga-se apenas o saldo restante 
            total_pago += saldo
            saldo = 0

        print(f"Mês {mes:2d}: Saldo restante R$ {saldo:8.2f}")
        mes += 1

    meses_totais = mes - 1
    print("-" * 45)
    print(f"Dívida quitada em {meses_totais} meses.")
    print(f"Total pago: R$ {total_pago:8.2f}")
    print(f"Total pago em juros: R$ {total_juros:8.2f}")