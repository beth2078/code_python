# Mean & Median

'''
Create a function for each statistical analysis tool: mean, and median. 
Each function should take a single list of integers as an argument, and 
then output the result.
'''

# Mean/ average
def mean():
    mean = 0
    user_input = 0
    sum_numbers = 0 
    counter = 1
    while user_input != 'x':
        user_input = input("Enter a number, x to exit: ")
        if user_input == 'x':
            break
        sum_numbers += int(user_input)
        mean = sum_numbers / counter
        counter += 1 
    print(f'mean  = {mean}')

# Median finder
def median():
    median = 0
    user_input = 0
    i = 0
    numbers = []
    leave = True
    while leave != False:
        user_input = input("Enter a number or x to exit: ")
        if user_input == 'x':
            leave = False
            break
        try:
            user_input = int(user_input)
        except:
            print("invalid input. moving on.")
        numbers.append(user_input)
        if i > len(numbers) - 1:
            break
        i += 1
    numbers.sort()
    print(numbers)
    if numbers[-1] % 2 == 0:
        median = ((len(numbers) /2) + (len(numbers) / 2 + 1)) /2
    else: 
        median = (len(numbers) + 1) / 2
    print (f'median = {median}')


init = input("Chose mean or median: ").lower()
if init == "mean":
    mean()
elif init == "median":
    median()
else:
    print("Invalid responce.")
