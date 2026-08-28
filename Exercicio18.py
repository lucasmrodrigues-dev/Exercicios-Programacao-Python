dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))

if divisor == 0:
    print("Erro: Não é possível dividir por zero!")
else:
    quociente = 0
    x = dividendo

    while x >= divisor:
        x = x - divisor
        quociente = quociente + 1

    resto = x

    print(f"{dividendo} / {divisor} = {quociente} (quociente) e {resto} (resto)")