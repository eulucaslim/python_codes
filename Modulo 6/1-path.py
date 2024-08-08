from pathlib import Path

p1 = Path('dados', 'teste.txt')
print(p1)

# tipo da variavel 
print(type(p1))

# Nome do Arquivo com o tipo
print(p1.name)

# Apenas o nome do arquivo
print(p1.stem)

# Apenas o tipo do arquivo
print(p1.suffix)

# Se o arquivo realmente existe
print(p1.exists())

if p1.exists():
    with open(p1, "r", encoding="utf-8") as file:
        print(file.read())
        
p2 = Path("dados")
print(list(p2.iterdir()))