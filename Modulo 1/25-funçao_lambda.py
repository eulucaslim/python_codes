#1 - Função de potencia de numeros
power = lambda num: num **2

# 2 - Função que verifica se o numero é par
pair = lambda x: x % 2 == 0 

# 3 - Função que divide o numero pelo outro
divNum = lambda x, y: x / y

# 4 - Função que inverte uma string
reverse = lambda s: s[::-1]

print(power(5))
print(power(9))
print(pair(27))
print(pair(30))
print(divNum(10,2))
print(divNum(6,2))
print(reverse('Python'))
print(reverse('JavaScript'))