'''
Write a function that counts the number of consonants in the given string argument. 
Assume that for simplicity, “aeiou” are the only set of vowels in English. 
The function should return an integer

Example → "blueberry" → 6 consonants (including y)
'''

def consonant_counter(text):
    i = 0
    counter = 0
    for i in range (1, len(text)):
        if text[i] == 'a':
            counter += 1
        elif text[i] == 'e':
            counter += 1
        elif text[i] == 'i':
            counter += 1
        elif text[i] == 'o':
            counter += 1
        elif text[i] == 'u':
            counter += 1
        # end of if statment
    # end of for loop
    consonants = len(text) - counter
    print(f'{text} has {consonants} cosonants.')
    return text
# end of function

text = consonant_counter(input("Enter a word: "))
