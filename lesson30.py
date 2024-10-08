# String Pattern Creator
'''
Write a function that takes an N integer greater than 0 
and outputs/prints the following pattern.
'''

def create_line(num):
    ''' returns a string  of 1 and 0  based on the argument
    
    arugument: 
        num: integer, to determine how long the string is 

    return:
        text: a series of 1 and 0's as a string 
    '''
   
    text = ''
    for i in range(1, num+1):
        if i % 2 == 0: 
            text += '0'
        else: 
            text += '1'
    return text

def output_pattern(num):
    for i in range(1, num+1):
        print(create_line(i))

number = int(input("Enter a number: "))
value = output_pattern(number)
print(value)