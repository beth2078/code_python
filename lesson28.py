#Palindrome Program Checker
'''
Write a function that returns True if the given string argument is a palindrome. 
Assume that the argument will only contain alphabetical characters. 

Example --> 'tacocat' is a palindrome. 'tacodog' is not a palindrome
'''

def palindrome_checker(palindrome):
    a = 0
    b = -1
    if palindrome[a] == palindrome[b]:
        print(f"{palindrome} is a palindrome.")
        while a < len(palindrome):
            a += 1
            b -= 1
    else: 
        print(f"{palindrome} is not a palindrome.")
    return palindrome

palindrome = palindrome_checker(input("Enter a word: "))      