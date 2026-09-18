#Escreva uma função chamada inverter_lista(lista) que receba uma lista de elementos e retorne uma nova lista com os mesmos elementos na ordem inversa.
def inverter_lista(lista):
    lista_invertida = []

    # Iteração do último índice até o índice 0
    for i in range(len(lista) - 1, -1, -1):
        lista_invertida.append(lista[i])

    return lista_invertida  # Fora do laço for


# Código de teste (fora da função)
numeros = [10, 20, 30, 40, 50]
resultado = inverter_lista(numeros)

print(f"Original : {numeros}")
print(f"Invertida : {resultado}")