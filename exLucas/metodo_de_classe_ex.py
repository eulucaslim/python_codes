class Identifier:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def register(cls, string):
        import re
        item = re.findall('é \w*', string)
        name = item[0][2:]
        age = item[1][2:]
        return cls(name, int(age))

name = Identifier.register('Meu nome é Lucas e minha idade é 18')
name2 = Identifier.register('Meu nome é Samuel e minha idade é 19')

print(name.__dict__)
print(name2.__dict__)