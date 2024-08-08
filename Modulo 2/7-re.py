import re # O r siginifica que estamos trabalhando com uma string bruta (ram string)

text = "OneBitCode: Transformamos pessoas em programadores sem limites"

# 1 - Índice inicial e final de palavras
match = re.search(r'sem limites', text)
print('Indice inicial ', match.start())
print('Indice final ', match.end())

# 2 - Buscando o índice que possui o ponto
site = "https://onebitcode.com"
# match = re.search(r'.', site)
match = re.search(r'\.', site)
print(match)

# 3 - Buscando uma lista de caracteres dentro de uma frase
pattern = "[a-m]"
result = re.findall(pattern, text)
print(text)
print(result)

# 4 - Verificando o início de uma string
rule = r"^A"
pharases = ['A casa está suja', 'O dia está lindo', 'Vamos passear']

for f in pharases:
    if re.match(rule, f):
        print(f'Corresponde: {f}')
    else:
        print(f'Não Corresponde: {f}')

# 5 - Verificando o final de uma string
rule_end = r'!$'
pharases2 = 'O dia está lindo !'
match = re.search(rule_end, pharases2)
if match:
    print('Sim, Corresponde')
else:
    print('Nao Corresponde')
