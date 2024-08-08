distancia = float(input('Qual a distancia em km, que o passagueiro percorreu? \n'))

if distancia <= 200:
    result = distancia * 0.5
else:
    result = distancia * 0.35

print(f'O preço da passagem é de R$ {result:.2f}')