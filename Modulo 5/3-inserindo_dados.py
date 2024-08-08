import sqlite3

# 1 - Conectando no BD
connection = sqlite3.connect('title.db')

# 2 - Criando um cursor
'''
Cursor é um integrador que permite navegar
e manipular os registros em um BD
'''

cursor = connection.cursor()

# 3 - Inserindo Dados
cursor.execute('''
    INSERT INTO movies (name, year, score)
    VALUES ('Super Mario Bros', 2023, 10)                        
               ''')

cursor.execute('''
    INSERT INTO movies (name, year, score)
    VALUES ('Avatar', 2023, 9.5)                        
               ''')

cursor.execute('''
    INSERT INTO movies (name, year, score)
    VALUES ('Velozes e Furiosos 10', 2023, 8.0)                        
               ''')

# 4 - Gravando Dados no BD
connection.commit()
print('Dados Inseridos com Sucesso')

# 5 - Fechando conexão
connection.close()