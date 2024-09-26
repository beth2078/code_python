# 0. Import
from math import ceil

# 1. Input 
section1 = input("Enter section 1: ")
section2 = input("Enter section 2: ")
section3 = input("Enter section 3: ")

#2. Processing 
cans = len(section1) + len(section2) + len(section3)
#len function --> counts how many characters in a string, and how many indexes in a set 

boxes = ceil(cans/12)
totalcost = 14.95 * boxes 
leftover = 12*boxes - cans  

#3. Output
print(f"The number of cans we need is {cans}.")
print(f'The number of boxes is: {boxes}.')
print(f'The total cost of all the paint is ${totalcost}.')
print(f'The number of leftover cans is {leftover}.')