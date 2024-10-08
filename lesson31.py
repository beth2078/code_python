# Anagram

'''
Create a function that checks if the two strings arguments are anagrams. 
The function should return True if the two strings are anagrams.
'''
# Solution 1
def anagram(word1, word2):
    if len(word1) != len(word2):
        return False # not an anagram
    else: 
        # look through all the letters
        for character in word1: 
            if word1.count(character) != word2.count(character):
                return False #also not an anagram
        # end of for loop
        return True
# end of anagram

# Solution 2
def anagram2(word1, word2):
    if len(word1) != len(word2):
        return False
    else: 
        list_word1 = sorted(word1)
        list_word2 = sorted(word2)
        #sorted sorts a string lexicographically and stores each individual
        # characters as items in a list
        for i, character in enumerate(list_word1):
            if list_word2[i] != character:
                return False
        # end of for loop
        return True

result1 = input("Enter a word: ")
result2 = input("Enter another word: ")
text = anagram2(result1, result2)
print(text)
