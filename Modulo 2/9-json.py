import json

# 1 - Strings para Dicionário
person = '{"name": "Rodrigo", "languagens": ["Python", "Javascript"]}'
person_dict = json.loads(person)
print(person_dict)
print(person_dict['languagens'])

# 2 - Convertendo dicionarios para Json
person_json = json.dumps(person_dict)
print(person_json)
print(type(person_json))
print(type(person_dict))

# 3 - Formatando Json
print(json.dumps(person_dict,indent=4, sort_keys=True))

# 4 - Salvando json em txt
with open('person.txt', "w") as json_file:
    json.dump(person_dict, json_file)

# 5 - Lendo json externo
with open('iris.json','r') as f:
    data = json.load(f)
    print(data)
