# Factor finder
'''
Create a function that returns a list of the integer argument's factor.

Example: 12 returns [1, 2, 3, 4, 6, 12]

Create a function that returns True if the given integer 
argument is a prime number.
'''

def factor_finder(): 
    pn = False
    i = 1
    j = 0
    factor_counter = 1
    user_input = int(input("Enter a number: "))
    factor = 0
    factor = user_input
    while pn == False:
        if factor % i == 0 and factor > 0:
            factor = int(user_input / i)
            print(f"{factor} is a factor of {user_input}")
            factor_counter += 1
        else:
            pn = True
        i += 1
        if user_input <= 0:
            print("Invalid input.")
    print(f'1 is a factor of {user_input}')
    if factor_counter > 2:
        print("This is not a prime number.")
    else:
        print("This is a prime number.")

factor_finder()