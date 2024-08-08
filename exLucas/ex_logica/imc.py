altura = float(input('Digite a sua altura em cm: \n'))
peso = float(input('Digite seu peso: \n'))

result = peso / (altura * altura)
print(f'Seu IMC é {result:.2f}')

if result < 18.5:
    print('Você está com Baixo Peso!')
    
elif result >= 18.5 and result <= 24.9:
    print('Você está com peso Normal :)')
    
elif result >= 25 and result <= 29.9:
    print('Você está Sobrepeso!')
    
elif result >= 30 and result <= 34.9:
    print('Você está com Obesidade Grau I')
    
elif result >= 35 and result <= 39.9:
    print('Você está com Obesidade Grau II')
    
elif result >= 40:
    print('Você está com Obesidade Grau III')
    