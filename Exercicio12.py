a = float(input("Primeiro número: "))
b = float(input("Segundo número: "))
operacao = input("Digite a operação a realizar (+, -, * ou /): ")

if operacao == "+":
    resultado = a + b
    print(f"Resultado: {resultado}")
elif operacao == "-":
    resultado = a - b
    print(f"Resultado: {resultado}")
elif operacao == "*":
    resultado = a * b
    print(f"Resultado: {resultado}")
elif operacao == "/":
    if b != 0:
        resultado = a / b
        print(f"Resultado: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida! Por favor, escolha entre +, -, * ou /.")