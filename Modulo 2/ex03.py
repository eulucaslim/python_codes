import re

def check_caracter(string):
    rule = re.compile(r'[^a-zA-Z0-9]')
    string = rule.search(string)
    return not bool(string)

print(check_caracter('webfwbeufwbd32#'))
print(check_caracter('webfwbeufwb'))