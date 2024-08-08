from agenda import list_contacts, add_contact, delete_contacts

def main():
    while True:

        print('----Agenda Telefônica----\n')
        print('1 - Adicionar Contato\n')
        print('2 - Listar Contatos\n')
        print('3 - Remover Contato\n')
        print('4 - Sair do Programa\n')
        
        choice = input('> ')
        
        if choice == '1':
            add_contact()
            print('Contato Adicionado com sucesso!')
            
        elif choice == '2':
            list_contacts()
        
        elif choice == '3':
            delete_contacts()
        
        elif choice == '4':
            print('Encerrando Programa...')
            break
            
        
        else:
            print('Esta opçao nao esta disponivel, tente novamente')

main()