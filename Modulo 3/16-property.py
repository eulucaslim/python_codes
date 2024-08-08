class Person:
    def __init__(self, name, age):
        self._name = name
        self.age = age
        
        # Get
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Nome deve ser uma string')
        self._name = value
            
pessoa = Person('Fulano', 12)
print(vars(pessoa))
    