salario = float(input("Digite o salário atual: R$ "))
porcentagem_aumento = float(input("Digite a porcentagem de aumento: "))

aumento = salario * porcentagem_aumento / 100
novo_salario = salario + aumento

print("\n--- Resultado ---")
print(f"Salário atual: R$ {salario:.2f}")
print(f"Percentual de aumento: {porcentagem_aumento:.2f}%")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")