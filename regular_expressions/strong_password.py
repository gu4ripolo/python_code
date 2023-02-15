import re

passwordRegex = re.compile(r'''
    ([a-zA-Z0-9!"$%&/?-_]{8})
''', re.VERBOSE)

passwords = ['secreto123', 'hola', 'Contras3na!muy_fu3rt3', 'demasiado-corta']

correct_passwords = []
incorrect_passwords = []

for password in passwords:
    if passwordRegex.search(password):
        correct_passwords.append(password)
    else:
        incorrect_passwords.append(password)

print("Contraseñas correctas: ", correct_passwords)
print("Contraseñas incorrectas: ", incorrect_passwords)