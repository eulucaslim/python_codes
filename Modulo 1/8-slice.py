gameName = "Fifa 23"
gameDescription = """
Fifa 23 é um jogo de futebol  desenvolvido pela EA Sports
e que possibilita jogar localmente ou online
"""

# string[inicio:fim] - índice começa na posica 0 | índice final -1

# 1 - Busque toda string a paartir da primeira posição
print(gameName[0:])

# 2 - Busque toda a string até a última posição
print(gameName[:7])

# 3 - Busque toda string da terceira ate a ultima posição
print(gameName[2:])

"""
string[inicio:fim:passo] - indice comeca na posição 0 | indice final -1
passo - determina o incremento. Por padrão esse é o número 1
"""

#4 -Busque toda a string de 2 em 2 caracteres
print(gameName[::2])

# 5 - Busque toda a string nos índices ímpares
print(gameName[1::2])

# 6 - Inverter uma string de trás para frente
print(gameName[::-1])
