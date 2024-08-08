import sqlite3

connection = sqlite3.connect('agenda.db')
cursor = connection.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS agenda (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone INTEGER NOT NULL
    );           
               ''')
connection.commit()
connection.close()

def add_contact():
    name = input('Nome: \n')
    phone = int(input('Número: \n'))
    
    connection = sqlite3.connect('agenda.db')
    cursor = connection.cursor()
    
    cursor.execute("""
        INSERT INTO agenda (name, phone)
        VALUES(? , ?)
                   """,(name, phone))
    
    connection.commit()
    print('Contato Adicionado com Sucesso!')
    connection.close()
    
def show_contats():
    connection = sqlite3.connect('agenda.db')
    cursor = connection.cursor()
    
    print('Contatos: \n')
    for row in cursor.execute('SELECT id, name FROM agenda'):
        print(f'{row}')
        
    id = int(input('Informe o id do contato que deseja visualizar \n'))
    
    cursor.execute('SELECT name, phone FROM agenda WHERE id = ?', (id,))
    contact = cursor.fetchone()
    
    if contact:
        print(f'\nNome: {contact[0]} \nTelefone: {contact[1]}\n')
    else:
        print('Contato não encontrado.')
    connection.close()
    
    
def update_contact():
    connection = sqlite3.connect('agenda.db')
    cursor = connection.cursor()
    print('Contatos na Agenda:')
    for row in cursor.execute('SELECT id, name FROM agenda'):
        print(f'{row}')
        
    id = int(input('Informe o id do contato que deseja atualizar \n'))
    name = input('Digite o nome do novo contato: \n')
    phone = int(input('Digite o numero novo do contato: \n'))
    
    cursor.execute('''
        UPDATE agenda set name = ?, phone = ?
        WHERE id = ?        
                   
                   ''', (name, phone, id ))
    
    connection.commit()
    print('Contato Atualizado com Sucesso!')
    connection.close()
    
def delete_contact():
    connection = sqlite3.connect('agenda.db')
    cursor = connection.cursor()
    print('Contatos na Agenda:')
    for row in cursor.execute('SELECT id, name FROM agenda'):
        print(f'{row}')
        
    id = int(input('Informe o id do contato que deseja remover \n'))
     
    cursor.execute('''
        DELETE FROM agenda
        WHERE id = ?          
                   ''', (id, ))
    
    connection.commit()
    print('Contato Removido com Sucesso!')
    connection.close()