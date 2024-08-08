# import random

# rd = random.randint(1,10)
# n = int(input('Advinhe um numero de 1 a 10: \n'))
# while n != rd:
#     if n != rd:
#         print('Errou o número!, Tente Novamente')
#         break

# if n == rd:
#     print('Você Acertou!!')
#     print('O numero escolhido era:', rd)

import random

done = False

while not done:
    print('O que deseja fazer?')
    print('1. Advinhar o número')
    print('2. Sair')
    
    choice = input('> ')
    
    if choice == "1":
        print("======Advinhe um número de 1 a 10======\n")
        number = int(input('Digite um numero de 1 a 10\n'))
        result = random.randint(1,10)
        if number == result:
            print("Parabéns. Você acertou!")
        else:
            print(f'Tente Novamente. O número sorteado foi {result}')
    
    elif choice == "2":
        print('Programa Encerrado...')
        done = True
        
    else:
        print('Opção Inválida, Insira um numero válido')
        