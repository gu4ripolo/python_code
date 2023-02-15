#! python3
# url.py - Finds urls on the clipboard

'''
Aquí hay algunas URLs de ejemplo que coincidirían con la expresión regular anterior
http://www.google.com
https://www.facebook.com
https://www.amazon.co.uk
http://www.nytimes.com/
https://www.youtube.com/watch?v=dQw4w9WgXcQ
'''

import pyperclip, re

urlRegex = re.compile(r'''(
    (https?)://
    (www\.)?
    [-a-zA-Z0-9@:%._\+~#=]{2,256}
    \.
    [a-z]{2,6}
    \b
    ([-a-zA-Z0-9@:%_\+.~#?&//=]*)
)''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())

matches = []
for groups in urlRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print("No url found.")