# 1 - Crie uma funçao que receba dois argumentod: o primeiro nome e o segundo nome
def full_name(fname, lname):
    print(f'Nome Completo: {fname} {lname}')

full_name('Rodrigo', 'Macedo')

# 2 - Crie uma funçao que some dois numeros via parametros
def sum(a, b):
    return a + b

print(sum(10,50))

# 3 - Argumentos default numa função
def address(country='Brasil'):
    print(f'Eu moro no {country}')
    
address()
address('Canadá')

# 4 - Avaliação do jogo
def rating_game(qtdRating):
    game_name = input('Digite o nome do jogo') 
    sum = 0 
    for i in range(qtdRating):
        note = float(input('Digite a nota para o jogo: \n'))
        sum += note
    print(f'A media de avalição do jogo {game_name} é {sum/qtdRating}')
    
rating = int(input('Digite quantas avaliações deseja fazer no jogo\n'))
rating_game(rating)
        