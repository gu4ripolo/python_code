# English to Pig Latin
print("Enter the english message to translate into pig latin:")
message = input('> ')

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatin = [] # Alist of the words in Pig Latin
for word in message.split():
    # Separate the non-letters at the start of this word:
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]        
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue
        
    # Separate the non-letters at the end of this word:
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]

    # Remember if the word was in uppercase or title case.
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower() # make the word lowercase for translation.

    # Separate the consonants at the start of this word:
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    # Add the Pig Latin ending to the word:
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

   # Set the word back to uppercase or title case:
    if wasUpper:
        word = word.upper()
    else:
        word = word.title()

    # Add the non-letters back to the start or end of the word.
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

# Join all the words back togheter into a single string:
print(' '.join(pigLatin))


   

