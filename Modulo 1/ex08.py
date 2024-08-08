def check_char(text):
    type = {"Uppercase": 0,"Lower": 0}
    for char in text:
        if char.isupper():
            type["Uppercase"] += 1
        elif char.islower():
            type["Lower"] += 1
    print("Texto original:", text)
    print("Letras maiusculas:",type["Uppercase"])
    print("Letras minusculas:",type["Lower"])
    
check_char("A Melhor forma de Prever o futuro é Criá-lo")