import sqlite3

# 1 - Criando o Banco de Dados
connection = sqlite3.connect('title.db')

# 2 - Verifica se ouve alterações na base de dados
print(connection.total_changes)