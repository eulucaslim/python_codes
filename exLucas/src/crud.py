from pymongo import MongoClient

client = MongoClient()

mydb = client['mercado']
col = mydb['lucro']
col2 = mydb['despesa']

def lucro():
    product = input('Digite o nome do produto: \n')
    vlr_product = float(input('Digite o valor do Produto: \n'))
    
    col.insert_one({"produto": product, "valor": vlr_product})
    
    
def despesa():
   product = input('Digite o nome do produto: \n')
   vlr_product = float(input('Digite o valor do Produto: \n'))
    
   col2.insert_one({"produto": product, "valor": vlr_product})

def extrato():
    print("Lucros:")
    for lucro in col.find():
        print(lucro)
    
    print("\nDespesas:")
    for despesa in col2.find():
        print(despesa)

def saldo_final():
    total_lucro = 0
    total_despesa = 0

    # Somar todos os lucros
    for lucro in col.find():
        total_lucro += lucro['valor']
    
    # Somar todas as despesas
    for despesa in col2.find():
        total_despesa += despesa['valor']
    
    # Calcular o saldo final
    saldo = total_lucro - total_despesa
    print(f"Saldo final do dia: {saldo}")