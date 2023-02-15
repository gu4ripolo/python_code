#! python3
# dates.py - Finds dates on the clipboard
# Not working

import re, pyperclip

dateRegex = re.compile(r'''(
    (\d{2}|\d{4})
    [.-/]
    (\d{2})
    [.-/]
    (\d{2}|\d{4})
)''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []
for groups in dateRegex.findall(text):
       dateRegex = '/'.join([groups[0], groups[1], groups[2]])
       matches.append(dateRegex)

# Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print("No dates found.")