import pprint

gamesDict = {
    'Resident evil 4': {
       'yearLaunch': 2023,
       'classification': 9.8,
       'genre':['ação', 'aventura'] 
    },
    
    'Mario Odyssey':{
       'yearLaunch': 2017,
       'classification': 10.0,
       'genre':['aventura', '3d']
    },
    
    'Donkey Kong Country': {
        'yearLaunch': 1995,
       'classification': 9.5,
       'genre':['aventura', 'plataforma']
    }  
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gamesDict)

# 1 - Buscar informação dentro de um dicionario aninhado
print(gamesDict['Mario Odyssey']['genre'])

# 2 - Adicionar um novo item
gamesDict["Mario Odyssey"]['players'] = 1
print(gamesDict["Mario Odyssey"])

# 3 - Excluir um dicionario
del gamesDict['Resident evil 4']
pp.pprint(gamesDict)