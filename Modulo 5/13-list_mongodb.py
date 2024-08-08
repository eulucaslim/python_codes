from pymongo import MongoClient
from pprint import pprint

client = MongoClient()

mydb = client.obcblog
mycol = mydb.posts

# Retorna Apenas um documento
# result = mycol.find_one()

# Retorna todos os documentos
result = mycol.find()

for r in result:
    pprint(r)