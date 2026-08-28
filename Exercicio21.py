soma = 0
quantidade = 0

while True:
    n = int(input("Digite um número inteiro (0 para sair): "))
    if n == 0:
        break
    soma = soma + n
    quantidade = quantidade + 1

if quantidade > 0:
    media = soma / quantidade
    print("\n--- RESUMO ---")
    print(f"Quantidade de números digitados: {quantidade}")
    print(f"Soma: {soma}")
    print(f"Média aritmética: {media:.2f}")
else:
    print("\nNenhum número válido foi digitado.")