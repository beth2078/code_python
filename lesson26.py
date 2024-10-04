# Function in python 3

#1. To create a function --> def function_name(arg1, arg2,...):
#2. Use triple quotation marks """ to write your docstrings
#3. Use the arguments started and creata a instruction set that solves a single problem
#4. Use return to return the data thats been processed by your function


def factor_count(number):
    """
    determines the number of factors the number has 

    Args: 
        number: an integer needed to determine the number of its factors

    Returns: 
        an intager: which is the totabl amount of factors and argument has
    """
    counter = 0
    for divider in range(1, number + 1):
        if number % divider == 0:
            counter += 1
    return counter
# end of factor count

#Problem: determine the number of factors for each number from 1 to n
#Let n be a user input

n = int(input("Enter the n value: "))

for num in range(1, n+1):
    factor_size = factor_count(num)

    print(f"{num} has {factor_size} factors")