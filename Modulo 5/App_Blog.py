from Blog import show_menu,add_user, add_post, query_users_posts

while True:
    show_menu()
    option = input('Selecione uma opção:\n')
    
    if option == '1':
        add_user()
    
    elif option == '2':
        add_post()
    
    elif option == '3':
        query_users_posts()
        
    elif option == '4':
        print('\nEncerrando Programa...')
        break
    
    else:
        print('Informe uma opção válida!')