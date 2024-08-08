class Register:
    # Módulo construtor
    def __init__(self, name, trip):
        self.name = name
        self.trip = trip
        
    # Utilizando o método estático
        
    @staticmethod
    def travel(trip):
        if trip == 'Portugal':
            confirm = ['Seu Cadastro foi realizado com sucesso !']
        
        elif trip == 'Califórnia':
            confirm = ['Seu Cadastro foi realizado com sucesso !']
            
        elif trip == 'Suiça':
            confirm = ['Seu Cadastro foi realizado com sucesso !']
        
        else:
            confirm = ['Sem passagens disponiveis para este local!']
        
        return confirm
    
    # Função para exibir os atributos da classe 
    def show_travel(self):
        return f'Nome: {self.name} \nViagem Realizada: {self.trip}'

name = input('Digite seu nome: \n') 
destino = input('Digite seu local de destino: \n')

registro = Register(name, destino)
          
print(Register.travel(destino))
print(registro.show_travel())