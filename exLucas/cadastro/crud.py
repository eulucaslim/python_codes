import os
import sqlite3
    
def menu():
    print('===== Cadastro Clientes ======')
    print('||  1. Cadastrar Cliente    ||')
    print('||  2. Login                ||')
    print('||  3. Exibir Cliente       ||')
    print('||  4. Sair do Programa     ||')
    print('\n')
    

def cadastrar():
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute("""
         CREATE TABLE IF NOT EXIST usuarios(
             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             email TEXT NOT NULL,
             password TEXT NOT NULL
         );
                  """)
    
    name = input('Nome: ')
    email = input('Email: ')
    password = input('Senha: ')
    
    cursor.execute("""
        INSERT INTO usuarios (name, email, password)
        VALUES (?, ?, ?)
                   """, (name, email, password))
    
    connection.commit()
    print('Usuário Adicionado com Sucesso!\n')
    connection.close()

def show_users():
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    
    data = cursor.execute("""
        SELECT name, email FROM usuarios
                          """)
    print(data.fetchall())
    
    
def delete():
    os.system("cls" if os.name == 'nt' else 'clear')
        
    