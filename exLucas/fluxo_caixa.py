fluxo_caixa = []

print('------ Fluxo de Caixa --------')
print('1 - Adicionar receita')
print('2 - Adicionar despesa')
print('3 - Sair do Programa')

def add_receita():
    nome = input('Nome:')
    valor = float(input('Valor:'))
    fluxo_caixa.append({
            'name':nome,
            'valor':valor  
        })

while True:
    choice = input('>')
    
    if choice  == '1':
        nome = input('Nome:')
        valor = float(input('Valor:'))
        fluxo_caixa.append({
            'name':nome,
            'valor':valor  
        })
    