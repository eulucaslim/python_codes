gameName = input('Digite o nome do jogo: \n')
qtdRating = 0
totalRating = 0
rating = 0
average = 0  

while(rating != -1):
    rating = float(input('Informe a nota do jogo: \n'))
    if (rating != -1):
        totalRating += rating
        qtdRating += 1
        average = totalRating / qtdRating   
print(f'A média de avaliaçoes do jogo {gameName} é de {average:.2f}') 