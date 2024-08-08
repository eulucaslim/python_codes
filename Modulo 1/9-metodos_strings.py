gameName = "Fifa 23"
gameDescription = """
Fifa 23 é um jogo de futebol,  desenvolvido pela EA Sports,
e que possibilita jogar localmente ou online
"""

print(gameName.upper()) # Retornar string em maiusculo
print(gameName.lower()) # Retornar string em minusculo
print(gameName.capitalize()) # Apenas a primeira letra em maiusculo
print(gameName.title()) # Apenas a primeira letra em maiusculo
print(gameName.center(10, "-")) # retorna a string centralizada com caracter de preenchimento
print(gameName.find("i")) # Retorna a posição de um determinado caractere
print(gameDescription.count("f")) # Conta os caracteres
print(gameDescription.count("a")) # Conta os caracteres
print(gameDescription.replace("Fifa", "Pes")) # Altera um elemnto por outro
print(gameDescription.split(",")) # quebra a linha


