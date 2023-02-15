import re

creditRegex = re.compile(r'''
 # Visa: comienza con 4 y tiene 16 dígitos
 # American Express: comienza con 34 o 37 y tiene 15 dígitos
 # MasterCard: comienza con 51-55 y tiene 16 dígitos
 # Discover: comienza con 6011 y tiene 16 dígitos
((4\d{3}|5[1-5]\d{2}|6011))   # Primer grupo de cuatro dígitos (Visa, AE O MC)  
[-\s]?                              # Un guión o un espacio es opcional
((\d{4}))                           # Primer grupo de cuatro dígitos
[-\s]?                              # Un guión o un espacio es opcional
((\d{4}))                           # Segundo grupo de cuatro dígitos
[-\s]?                              # Un guión o un espacio es opcional
((\d{4}))                            # Tercer grupo de cuatro dígitos
''', re.VERBOSE)

text = '''
Este es un texto que contiene algunas tarjetas de crédito válidas:
- Visa: 4532782001745862, 4916936759003588, 4485611256655086
- Mastercard: 5560100267077316, 5204036791109389, 5342152671352442
- Discover: 6011230724558622, 6011019474150555, 6011969791441183
'''

text_hidden =  creditRegex.sub(r'\1 **** **** ****', text)

print(text_hidden)