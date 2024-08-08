import sqlite3

# 1 - Conectando no BD
connection = sqlite3.connect('title.db')

# 2 - Criando um cursor
'''
Cursor é um integrador que permite navegar
e manipular os registros em um BD
'''
cursor = connection.cursor()

# 3 - Solicitando Dados do Usuário
id = int(input('Informe o id do filme que deseja atualizar\n'))
name = input('Informe o novo nome do filme: \n')

# 4 - Atualizando Dados
cursor.execute("""
    UPDATE movies set name = ?           
    WHERE id = ?           
               """, (name, id))

connection.commit()
print('Dados atualizados com sucesso')

# 5 - Fechando conexão
connection.close()