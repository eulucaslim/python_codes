gamesList = ["Resident Evil 4", "Star Wars Jedi Survivor", 
             "The Legendo of Zelda", "Red Dead 2", "Mario Odyssey", "Luigis Mansion 3"]

# 1- Tamanho da lista
print(len(gamesList))

# 2 - Recupoerar um item da lista pelo índice
print(gamesList.index("Mario Odyssey"))

# 3 - Adicionar item ao final da lista
gamesList.append("Gta V")
print(gamesList)

# 4 - Ordenar a lista 
gamesList.sort()
print(gamesList)

# 5 -Copiar itens de uma lista para outra, e remover 
gameReset = gamesList.copy()
gameReset.remove("Star Wars Jedi Survivor")
print(gameReset)

# 6 - Remove todos os itens da lista
gamesList.clear()
print(gamesList)