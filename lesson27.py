# String Cleaning Function
"""
Write a function that removes non-aphabethical characters from the given string 
and returns it as a lowercase versuin of the cleaned string. 

Example --> 'H E L L 0O!' = 'hello'

Function:
1 argument string

Returns: 
1 string object

Solution planning
1. the function should take a single argument and return a string 
2. look through each character of the string ... grab only alpha characters 
or remove non-alphacharacters
3. grow an empty string to a string filled with the alphabet

String method to use: .isalpha() ... returns True if the string has only "letters"
characters from the ASCII table
"""

def string_cleaner(text):
    ''' this function will take out all of non-alphabetical values from an input

    Arguments:
        word: user input used to determine if there are any non-alphabetical characters

    Return: 
        a string: this word outputs a string value 
    '''
    result = ''
    for character in text:
        if character.isalpha():
            result += character.lower() 
    return result


newWord = string_cleaner(input("Enter a word: "))
print(f'The New Word is: {newWord}')
