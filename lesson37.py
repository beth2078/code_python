'''
Implement a function that performs basic string compression using 
the counts of repeated characters. Return the string if the 
compression is longer or the same length as the argument.

For example, "aabcccccaaa" would become "a2b1c5a3"
'''

def str_zip(text):
    result = ' '
    ctr = 1
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            ctr +=1
        else:
            result += text[i-1]
            result += str(ctr)
            ctr = 1
    result += text[-1] + str(ctr)
    if len(result) < len(text):
        return result
    else:
        return text
# end of string_compressor

user_input = input("Enter any number of alpabet characters: ")
# expecting "a2b1c5a3"
print(str_zip(user_input))