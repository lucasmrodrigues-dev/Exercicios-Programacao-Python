cigarros_por_dia = int(input("Quantidade de cigarros fumados por dia: "))
anos_fumando = float(input("Quantidade de anos fumando: "))

minutos_perdidos_por_cigarro = 10
minutos_por_dia = 24 * 60
dias_por_ano = 365

total_minutos_perdidos = (
    anos_fumando
    * dias_por_ano
    * cigarros_por_dia
    * minutos_perdidos_por_cigarro
)

total_dias_perdidos = total_minutos_perdidos / minutos_por_dia

print("\n--- Resultado ---")
print(f"Estimativa de tempo de vida perdido: {total_dias_perdidos:.2f} dias")