valor = float(input("Digite o valor da casa: R$ "))
salario = float(input("Digite o salário: R$ "))
anos = int(input("Quantos anos para pagar: "))

meses = anos * 12
prestacao = valor / meses
limite_prestacao = salario * 0.3

if prestacao > limite_prestacao:
    print("\nInfelizmente, você não pode obter o empréstimo!")
    print(f"A prestação seria de R$ {prestacao:.2f}, superando o limite de R$ {limite_prestacao:.2f} (30% do salário).")
else:
    print("\nEmpréstimo APROVADO!")
    print(f"Valor da prestação mensal: R$ {prestacao:.2f}")