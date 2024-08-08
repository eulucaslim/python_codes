from crud import cadastrar, menu, show_users, delete

while True:
    menu()
    
    choice = input('Digite uma opção: ')
    
    if choice == "1":
        cadastrar()
    elif choice == "2":
        pass
    elif choice == "3":
        show_users()
    elif choice == "4":
        delete()
        print("\nÉ nós chefe...")
        break
    else:
        delete()
        print('Insira um número válido!\n')
    