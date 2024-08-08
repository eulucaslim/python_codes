"""
Fatorial de um numero:
3 -> 3 * 2 * 1
5 -> 5 * 4 * 3 * 2 * 1
"""
# 1 - Fatorial de um numero
def factorial(num):
    if num == 1:
        return 1
    else:
        return (num * factorial(num - 1))
    
number = int(input('Digite um numero para o fatorial\n'))
print(f'o fatorial de {number} é: {factorial(number)}')

# 2 - Soma total de um  numero
def sum_total(num):
    if num == 1:
        return 1
    else : 
        return(num + sum_total(num - 1))
    
number1 = int(input('Digite o numero que mostrará a soma total dele:'))
print(f'A soma total de {number1} é {sum_total(number1)}')