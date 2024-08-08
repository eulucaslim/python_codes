name  = input("Digite o nome do jogo:\n")
yearLaunch = int(input("Digite o ano de lançamento do jogo: \n"))
gamePrice = float(input("Digite o valor do jogo: \n"))
planIncluded = input("Esta incluso no serviço local?\n")

print("###Dados do Jogo###")
print("====================")
#Alternativa 1
# print("Nome do jogo: ", name)
# print("Ano do jogo: ", yearLaunch)
# print("Preço do jogo: ", gamePrice)
# print("Esta incluso no plano?", planIncluded)

#Alternativa 2
# print("Nome do Jogo: ", name, "\nAno de Laçamento:", yearLaunch, 
#        "\nPreço do jogo:", gamePrice, "\nEstá includo no serviço?", planIncluded)

#Alternativa 3
print(f"Nome do Jogo: {name} \nAno Laçamento: {yearLaunch} \nPreço do Jogo: {gamePrice} \nEstá incluso no plano: {planIncluded}")