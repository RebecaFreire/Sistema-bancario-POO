CAMINHO_EXTRATO = "extrato.txt"

class ContaBancaria:
    def __init__(self, limite=500.0, limite_saques=3):
        self.saldo = 0.0
        self.limite = limite
        self.limite_saques = limite_saques
        self.numero_saques = 0
        self.extrato = ""

    def salvar_extrato(self, movimento):
        with open(CAMINHO_EXTRATO, "a", encoding="utf-8") as f:
            f.write(movimento + "\n")

    def registrar_movimento(self, tipo, valor):
        movimento = f"{tipo}: R$ {valor:.2f}"
        self.extrato += movimento + "\n"
        self.salvar_extrato(movimento)

    def depositar(self, valor):
        if valor <= 0:
            print("Operação falhou! O valor do depósito deve ser positivo.")
            return
        self.saldo += valor
        self.registrar_movimento("Depósito", valor)

    def sacar(self, valor):
        if valor <= 0:
            print("Operação falhou! O valor do saque deve ser positivo.")
        elif valor > self.saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif valor > self.limite:
            print("Operação falhou! O valor excede o limite por saque.")
        elif self.numero_saques >= self.limite_saques:
            print("Operação falhou! Número de saques excedido.")
        else:
            self.saldo -= valor
            self.numero_saques += 1
            self.registrar_movimento("Saque", valor)

    def exibir_extrato(self):
        print("\n========= EXTRATO =========")
        print(self.extrato if self.extrato else "Não foram realizadas movimentações.")
        print(f"\nSaldo atual: R$ {self.saldo:.2f}")
        print("===========================\n")

def obter_valor(mensagem):
    entrada = input(mensagem).strip()
    try:
        valor = float(entrada.replace(",", "."))
        return valor
    except ValueError:
        print("Operação falhou! Digite um valor numérico válido.")
        return None

def main():
    conta = ContaBancaria()

    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """

    while True:
        opcao = input(menu).lower()

        if opcao == "d":
            valor = obter_valor("Informe o valor do depósito: ")
            if valor is not None:
                conta.depositar(valor)

        elif opcao == "s":
            valor = obter_valor("Informe o valor do saque: ")
            if valor is not None:
                conta.sacar(valor)

        elif opcao == "e":
            conta.exibir_extrato()

        elif opcao == "q":
            print("Saindo do sistema bancário. Até logcdo!")
            break

        else:
            print("Operação inválida. Escolha novamente.")
if __name__ == "__main__":
    main()

    conta = ContaBancaria()
    conta.registrar_movimento("Depósito", 500)
    conta.registrar_movimento("Saque", 150)
    print("Movimentos registrados com sucesso!")

