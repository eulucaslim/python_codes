from contact import Contact
from contactbook import ContactBook

contato_agenda = ContactBook()

while True:
    print('\n --- Opções Agenda de Contato ---')
    print('1. Adicionar Contato')
    print('2. Remover Contato')
    print('3. Listar Contatos')
    print('4. Buscar Contato')
    print('5. Sair')
    
    choice = input('Escolha a opção:\n')
    
    if choice == '1':
        name = input('Digite o nome:\n')
        phone = input('Digite o seu numero:\n')
        email = input('Digite o email:\n')
        
        contact = Contact(name, phone, email)
        contato_agenda.add_contact(contact)
        print('Contato Adicionado com sucesso\n')
        
    elif choice == '2':
        name = input('Digite o nome de quem será removido:\n')
        contact = contato_agenda.search_contact(name)
        if contact:
            contato_agenda.remove_contact(contact)
            print('Contato removido com sucesso\n')
    
    elif choice == '3':
        contato_agenda.display_contact()
        
    elif choice == '4':
        name = input('Digite o contato que deseja:\n')
        contact = contato_agenda.search_contact(name)
    
    elif choice == '5':
        break
    
    else:
        print('Este número não corresponde, Tente Novamente! \n')
        