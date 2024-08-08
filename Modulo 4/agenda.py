def add_contact():
    name = input('Digite o nome do contato: \n')
    address = input('Informe o endereço: \n')
    phone = input('Informe seu numero: \n')
    
    contact = f'Nome: {name} \nEndereço: {address} \nTelefone: {phone}\n'
    with open('dados/contatos.txt', 'a', encoding='utf-8') as file:
        file.write(contact)
            
            
def list_contacts():
    
    with open('dados/contatos.txt', 'r', encoding='utf-8') as file:
        contacts = file.read()
    print('Lista de Contatos:')
    print(contacts)
    
def delete_contacts():
    with open('dados/contatos.txt', 'w', encoding='utf-8') as file:
        file.write('')
    
    print('Contatos excluidos com sucesso!')
    
        
        
