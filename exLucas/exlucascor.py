# Dicionário 
mercados = {}
# Encerrador do programa 
done = False

# Função para listar os mercados
def print_mercados():
    print('Mercados Listados:')
    for i, mercado in enumerate(mercados.values()):
        print(f"{i+1}. {mercado['name']} ({len(mercado['products'])} produtos)")

# Função para exibir os produtos do mercado 
def print_products_mercado(mercado):
    print(f'Produtos do {mercado["name"]}:')
    for i, product in enumerate(mercado['products']):
        print(f'{i+1}. {product}')

# Laço de repetição para o mercado
while not done:
    print('##### Seja Bem-Vindo ao Centro de Mercados #####\n')
    print('1 - Adicionar um Mercado')
    print('2 - Remover um Mercado')
    print('3 - Listar Mercados')
    print('4 - Adicionar um produto em um Mercado')
    print('5 - Remover um produto de um Mercado')
    print('6 - Listar produtos de um Mercado')
    print('7 - Sair do Programa\n')

    choice = input("> ")

    # Caso 1 - Irá adicionar um mercado no Centro
    if choice == "1":
        mercado_name = input("Digite o nome do Mercado\n")
        mercados[mercado_name] = {'name': mercado_name, 'products': []}
        print('Mercado adicionado ao Centro!\n')

    # Caso 2 - Irá exibir os mercados disponíveis e poderá removê-lo    
    elif choice == "2":
        print_mercados()
        
        mercado_num = int(input("Digite a posição do mercado que deseja remover\n"))
        
        if mercado_num <= len(mercados):
            mercado_name = list(mercados.keys())[mercado_num - 1]
            del mercados[mercado_name]
            print("Mercado Removido...")
        
        else:
            print("Opção Inválida")
        
    # Caso 3 - Irá exibir os mercados disponíveis e listá-los 
    elif choice == "3":
        print_mercados()
    
    # Caso 4 - Irá exibir os mercados disponíveis e poderá adicionar um item no mercado escolhido
    elif choice == "4":
        print_mercados()
        
        mercado_num = int(input("Digite o número do Mercado que você deseja adicionar um produto: \n"))
        
        if mercado_num <= len(mercados):
            mercado_name = list(mercados.keys())[mercado_num - 1]
            product_name = input("Digite o nome do produto: \n")
            mercados[mercado_name]['products'].append(product_name)
            print("Produto Adicionado ao Mercado")
        else:
            print('Número do Mercado Inválido')
    
    # Caso 5 - Irá exibir os mercados disponíveis e poderá remover um item no mercado escolhido
    elif choice == "5":
        print_mercados()
        mercado_num = int(input("Digite o número do mercado: \n"))
        
        if mercado_num <= len(mercados):
            mercado_name = list(mercados.keys())[mercado_num - 1]
            product_num = int(input("Digite o número do produto: \n"))
        
            if product_num <= len(mercados[mercado_name]["products"]):
                del mercados[mercado_name]['products'][product_num - 1]
                print("Produto Removido com Sucesso!")
            else:
                print("Número do Produto Inválido")
        else:
            print("Número do Mercado Inválido")
    
    # Caso 6 - Irá listar os mercados disponíveis e poderá exibir os itens do mercado escolhido    
    elif choice == "6":
        print_mercados()
        mercado_num = int(input("Digite o número do mercado que deseja listar os itens: \n"))
        
        if mercado_num <= len(mercados):
            mercado_name = list(mercados.keys())[mercado_num - 1]
            print_products_mercado(mercados[mercado_name])
        
        else:
            print("Número do Mercado Inválido")
    
    # Caso 7 - Irá encerrar o programa, quando for escolhido
    elif choice == "7":
        done = True
        print("Programa Encerrado...\n")
              
    else:
        print("Opção Inválida, Tente Novamente")