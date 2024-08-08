import sqlite3

# 1 - Conectando no BD
connection = sqlite3.connect('title.db')

# 2 - Criando um cursor
'''
Cursor é um integrador que permite navegar
e manipular os registros em um BD
'''
cursor = connection.cursor()

# 3 - Lendo Dados da Tabela

data = cursor.execute("""
    SELECT * FROM movies                  
                      """)

print(data.fetchall())

# 4 - Iterando os Dados
for row in cursor.execute('SELECT * FROM movies'):
    print(f'{row} \n')
    
    
# 5 - Ordenando os Dados pelo score
for row in cursor.execute('SELECT * FROM movies ORDER BY score desc'):
    print(f'{row}')


# 6 - Fechando conexão
connection.close()