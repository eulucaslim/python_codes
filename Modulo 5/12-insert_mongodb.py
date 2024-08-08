from pymongo import MongoClient

client = MongoClient()

mydb = client.obcblog
mycol = mydb.posts

post1 = {
    "title": "FastApi",
    "category": "Backend",
    "author": {
        "name": "Rodrigo",
        "email": "Rodrigo@email.com"
    }
}

result = mycol.insert_one(post1)
print("Documento incluído com Sucesso!")
