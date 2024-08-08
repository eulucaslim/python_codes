from ex03_res import Restaurant

prate0 = Restaurant('Macarronada')
prate1 = Restaurant('X-Salada')
prate2 = Restaurant('Frango Grelhado')
prate3 = Restaurant('Lasanha')

print('Olá! Seja Bem-Vindo(a) ao Dominos Restaurante')
client = input('Qual seu nome ? \n')
print(f'{client} Temos estas opções:'
      """
      [0] - Macarronada
      [1] - X-Salada
      [2] - Frango Grelhado
      [3] - Lasanha
      """)

choice = int(input('O que você deseja ?'))
list_food = [prate0, prate1, prate2, prate3]

for option in list_food:
    if choice >= 4:
        print('O valor não corresponde')
        break
    else:
        print('Seu Pedido está indo para o preparo!')
        print(f'Nome: {client} \nSeu Pedido: {list_food[choice].food} ')
        break
