#Crie uma classe chamada ContaBancaria com os atributos titular e saldo (iniciando em 0.0). Crie dois métodos:

#depositar(valor): adiciona o valor ao saldo.

#exibir_saldo(): mostra quanto dinheiro há na conta.

class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0.0  # O saldo começa zerado por padrão

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser maior que zero.")

    def exibir_saldo(self):
        print(f"Titular: {self.titular} | Saldo Atual: R$ {self.saldo:.2f}")

# --- Testando a Classe ---

# Criando a conta do Carlos
minha_conta = ContaBancaria("Carlos")

# Verificando o saldo inicial
minha_conta.exibir_saldo()

# Fazendo um depósito
minha_conta.depositar(150.50)

# Verificando o saldo atualizado
minha_conta.exibir_saldo()