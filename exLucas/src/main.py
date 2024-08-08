from crud import lucro, despesa, extrato, saldo_final


while True:
    print('--- Mercadinho do Luquinhas ---')
    print('1. Adicionar Lucro')
    print('2. Adicionar Despesa')
    print('3. Extrato do Dia')
    print('4. Saldo Final')
    print('5. Sair do Programa')
    
    choice = input('Escolha uma opção: \n')
    
    if choice == "1":
        lucro()
        
    elif choice == "2":
        despesa()
    
    elif choice == "3":
        extrato()
        
    elif choice == "4":
        saldo_final()
    
    elif choice == "5":
        print('Encerrando programa...')
        break
    
    else:
        print("Insira uma opção válida!")