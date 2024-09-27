#Quadrant Selection 

#1. Input
point = input() # in a format of: "10 -11"
point = point.split(' ') # we are running the .split() from the string object class, and argument is a whitespace

# fixed_point = []
# for value in point:
#     fixed_point.append(int(value))

point = list(map(int, point))
# this will make these numbers as integers and not strings 
print(point)

#2. Variable unpacking
x, y = point
print(f'x is {x}')
print(f'y is {y}')

#3. Quadrant Selection
if x == 0 and y == 0:
    print("This is the origin.")
else: 
    if x > 0:
        #pass
        #this is a palceholder code in python
        if y > 0:
            print(f'The point of ({x}, {y}) is in Quadrant 1.')
        else: 
            print(f'The point of ({x}, {y}) is in Quadrant 4.')
    else: 
        if y > 0:
            print(f'The point of ({x}, {y}) is in Quadrant 2.')
        else:
            print(f'The point of ({x}, {y}) is in Quadrant 3.')