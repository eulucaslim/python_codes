class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def __str__(self):
        return f'Produto {self.name} - R$ {self.price} reais'
        
    def discount(self,perc_discount):
        ValorDiscount = (self.price/100) * perc_discount
        finalPrice = self.price - ValorDiscount
        return int(finalPrice)
    
macarrao = Product('Macarrão', 10)
print(macarrao)
print(macarrao.discount(10))
