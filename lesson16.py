#FizzBuzz

for num in range(1, 51): #for loop are finite loops that have a set end value
    if num % 5 == 0 and num % 3 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)
    # end of if 
# end of for loop