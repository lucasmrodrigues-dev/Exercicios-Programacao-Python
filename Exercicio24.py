# Encontre o maior e o menor número de uma lista sem usar max() e min().
numeros = [10 , 100, 1, 20, 50]

maior = numeros[0]
menor = numeros[0]

for n in numeros:
    if n > maior:
        maior = n
    if n < menor:
        menor = n

print("Maior: ", maior)
print("Menor: ", menor)
