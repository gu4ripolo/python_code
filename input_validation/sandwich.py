import pyinputplus as pyip

# Define los tipos de pan, proteínas, quesos y extras disponibles
breadType = ['integral', 'blanco', 'trigo']
proteinType = ['pollo', 'pavo', 'jamon', 'tofu']
cheeseType = ['manchego', 'oaxaca', 'panela']
extraType = ['mayonesa', 'mostaza', 'lechuga', 'tomate']

# Solicita al usuario el tipo de pan
bread = pyip.inputMenu(breadType, prompt="Escoge un tipo de pan:\n")

# Solicita al usuario el tipo de proteína
protein = pyip.inputMenu(proteinType, prompt="Escoge una proteina:\n")

# Pregunta si el usuario desea agregar queso
cheeseBool = pyip.inputYesNo(yesVal='si', noVal='no', prompt="¿Quieres queso en tu sandwich?\n")

# Si el usuario desea agregar queso, solicita el tipo de queso
if cheeseBool == 'si':
    cheese = pyip.inputMenu(cheeseType, prompt="¿Escoge un tipo de queso:\n")
else:
    cheese = "Sin queso"

# Pregunta si el usuario desea agregar ingredientes extras
extrasBool = pyip.inputYesNo(yesVal='si', noVal='no', prompt='¿Quieres ingredientes extras en tu sandwich?\n')

# Si el usuario desea agregar ingredientes extras, solicita el tipo de ingrediente extra
if extrasBool == 'si':
    extras = pyip.inputMenu(extraType, prompt="¿Escoge un ingrediente extra:\n")
else:
    extras = "Sin ingredientes extras"

# Solicita al usuario la cantidad de sandwiches que desea
cantidadSandwiches = pyip.inputInt(min=1, max=10, prompt="¿Cuantos sandwiches quieres?\n")

# Si el usuario solicita un solo sandwich, muestra el texto en singular, si solicita más de uno, en plural
if cantidadSandwiches == 1:
    sandwiches = "1 sandwich"
else:
    sandwiches = str(cantidadSandwiches) + " sandwiches"

# Muestra el resultado final de la orden del usuario
print("\n\nTu orden es la siguiente:")
print(f"\t{sandwiches} de {bread} con {protein}, {cheese} y {extras}.")
