while True:
    print("""
--- MENU ---
1 - Adição
2 - Subtração
3 - Divisão
4 - Multiplicação
5 - Sair
""")
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 5:
        print("Saindo do programa... Até logo!")
        break
    elif 1 <= opcao < 5:
        n = int(input("Tabuada de: "))
        x = 1
        
        print(f"\n--- TABUADA DO {n} ---")
        while x <= 10:
            if opcao == 1:
                print(f"{n} + {x} = {n + x}")
            elif opcao == 2:
                print(f"{n} - {x} = {n - x}")
            elif opcao == 3:
                print(f"{n} / {x} = {n / x:.2f}")
            elif opcao == 4:
                print(f"{n} x {x} = {n * x}")
            x = x + 1
    else:
        print("Opção inválida! Por favor, escolha um número de 1 a 5.")