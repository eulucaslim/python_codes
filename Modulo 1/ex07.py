num = int(input('Tabuada de: \n'))
begin = int(input('De: \n'))
end = int(input('Até: \n'))

x = begin 

while x <= end:
    print(f'Tabuada de {num} x {x} = {num * x}')
    x += 1