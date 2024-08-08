# 1- Função para imprimir o hello world
def wellcome():
    print('Hello World')
    
wellcome()

# 2 - Função para somar dois numeros
def sum():
    # print(5+4)
    return 5 + 4
    
print(sum())

# 3 - Funçao para cadastrar um jogo
def creat_game():
    name = input("Digite o nome do jogo:\n")
    yearLaunch = int(input("Digite o ano de lançamento do jogo: \n"))
    gamePrice = float(input("Digite o valor do jogo: \n"))
    noteRating = float(input("Digite a nota de avaliação do jogo:\n"))   
    
    print(f'{name} - R$ {gamePrice}')
    
creat_game()
creat_game()