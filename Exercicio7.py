quilometros = float(input("Digite a quantidade de quilômetros percorridos: "))
dias_aluguel = int(input("Digite quantos dias você ficou com o carro: "))

preco_por_dia = 60.00
preco_por_km = 0.15

custo_dias = dias_aluguel * preco_por_dia
custo_quilometros = quilometros * preco_por_km

total_a_pagar = custo_dias + custo_quilometros

print("\n--- Resultado ---")
print(f"Valor pelos dias: R$ {custo_dias:.2f}")
print(f"Valor pelos quilômetros: R$ {custo_quilometros:.2f}")
print(f"Total a pagar: R$ {total_a_pagar:.2f}")
