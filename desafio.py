# Menu de operações
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Variáveis iniciais
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Loop principal
while True:
    # Exibe o menu e recebe a opção do usuário
    opcao = input(menu).strip().lower()  # Remove espaços extras e converte para minúsculo
    
    # Deposito
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        
        # Verifica se o valor do depósito é válido
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    # Saque
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        # Verifica as condições para realizar o saque
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    # Extrato
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    
    # Sair
    elif opcao == "q":
        print("Saindo...")
        break
    
    # Opção inválida
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
