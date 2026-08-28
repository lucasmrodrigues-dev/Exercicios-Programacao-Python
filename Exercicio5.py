distancia = float(input("Digite a distância em km: "))
velocidade_media = float(input("Digite a velocidade média em km/h: "))

tempo_horas = distancia / velocidade_media

# Conversão do tempo para horas, minutos e segundos
tempo_total_segundos = int(tempo_horas * 3600)

horas = tempo_total_segundos // 3600
minutos = (tempo_total_segundos % 3600) // 60
segundos = tempo_total_segundos % 60

print("\n--- Resultado ---")
print(f"Tempo estimado: {tempo_horas:.2f} horas")
print(f"Tempo da viagem: {horas:02d}:{minutos:02d}:{segundos:02d}")
