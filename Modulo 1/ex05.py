salario = float(input('Digite seu salário: \n'))

if salario > 1.250:
    aumento = salario * 0.10
    salario += aumento
else:
    aumento = salario * 0.15
    salario += aumento

print(f'Seu aumento foi de R$ {aumento:.2f}')