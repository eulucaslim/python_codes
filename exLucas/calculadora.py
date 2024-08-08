from calc import sum, sub, mult, div

def main():
    while True:
        print('----Calculadora em Python----')
        print('Escolha uma opção:')
        print('Soma (+)')
        print('Subtração (-)')
        print('Multiplicação (*)')
        print('Divisão (+)')
        print('Sair do programa (5)')
        
        choice = input('Digite a sua opção: \n')
        
        if choice == '+':
            sum()
            
        elif choice == '-':
            sub()
            
        elif choice == '*':
            mult()
            
        elif choice == '/':
            div()
            
        elif choice == '5':
            print('Programa Encerrado...')
            break
        
        else:
            print('Digite uma opção válida!')

main()