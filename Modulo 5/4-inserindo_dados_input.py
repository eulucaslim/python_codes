import sqlite3

# 1 - Conectando no BD
connection = sqlite3.connect('title.db')

# 2 - Criando um cursor
'''
Cursor é um integrador que permite navegar
e manipular os registros em um BD
'''

cursor = connection.cursor()

# 3 - Solicitando dados do usuário
name = input('Nome do Filme: \n')
year = int(input('Digite o ano do Filme: \n'))
score = float(input('Nota do Filme: \n'))

# 4 - Inserindo dados 
cursor.execute("""
    INSERT INTO movies (name, year, score)
    VALUES (?, ?, ?)
               """, (name, year, score))

# 5 - Gravando Dados no BD
connection.commit()
print('Dados Inseridos com Sucesso')

# 6 - Fechando conexão
connection.close()