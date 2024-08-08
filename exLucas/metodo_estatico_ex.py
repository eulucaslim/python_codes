class SuperMercado:
    def __init__(self, name, marketplace):
        self.name = name
        self.marketplace = marketplace
    
    @staticmethod
    def products_market(marketplace):
        if marketplace == 'Bastos':
            products = ['Pão', 'Bolo', 'Queijo', 'Presunto']
        
        elif marketplace == 'Bom Preço':
            products = ['Salgados', 'Manteiga', 'Bolacha']
        
        else: 
            products = ['A definir']
        
        return f'Produtos vendidos: {products}'
    
market = input('Digite o nome do Mercado que deseja: ')

print(SuperMercado.products_market(market))