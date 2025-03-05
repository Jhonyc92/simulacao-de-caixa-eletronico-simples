# Define o saldo inicial da conta
saldo = 1000.00  

# Inicia um loop infinito que continuará até que o usuário escolha a opção de sair
while True:
    
    # Imprime as opções do menu disponíveis para o usuário
    print("\nCaixa Eletrônico")
    print("1 - Verificar Saldo")
    print("2 - Depositar Dinheiro")
    print("3 - Sacar Dinheiro")
    print("4 - Sair")
    
    # Solicita que o usuário escolha uma opção
    opcao = input("Escolha uma opção (1-4): ")  

    # Verifica a opção escolhida pelo usuário e executa a ação correspondente
    if opcao == '1':
        
        # Imprime o saldo atual da conta
        print(f"Seu saldo é: R$ {saldo:.2f}")  
        
    elif opcao == '2':
        
        # Solicita o valor do depósito
        deposito = float(input("Digite o valor do depósito: R$ "))  
        
        # Verifica se o valor do depósito é positivo
        if deposito > 0:  
            
            #saldo = saldo + deposito
            # Adiciona o valor do depósito ao saldo
            saldo += deposito  
            # Confirma o depósito
            print(f"Depósito de R$ {deposito:.2f} realizado com sucesso!")  
            
        else:
            
            # Informa que o valor do depósito é inválido
            print("Valor de depósito inválido.")  
            
    elif opcao == '3':
        
        # Solicita o valor do saque
        saque = float(input("Digite o valor do saque: R$ "))  
        
        # Verifica se o valor do saque é válido e se há saldo suficiente
        if saque > 0 and saque <= saldo:  
            
            # Subtrai o valor do saque do saldo
            saldo -= saque  
            
            # Confirma o saque
            print(f"Saque de R$ {saque:.2f} realizado com sucesso!")  
            
        else:
            
            # Informa que o valor do saque é inválido ou que não há saldo suficiente
            print("Valor de saque inválido ou saldo insuficiente.")  
    
    elif opcao == '4':
    
        # Agradece o usuário e prepara-se para sair do loop
        print("Obrigado por utilizar o nosso caixa eletrônico. Até mais!")  
        
        # Sai do loop, terminando o programa
        break  
    
    else:
    
        # Informa ao usuário que ele escolheu uma opção inválida e continua o loop
        print("Opção inválida. Por favor, tente novamente.")  
            
