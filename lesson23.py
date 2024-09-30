#Average Calculator
#mean = sum of data / by the amount of data 
loop = True

total_sum = 0
counter = 0

# input
while loop:
    # as long as the loop is equal to true it keeps runing 
    user_input = input("Enter the mark  -OR- \"Exit\" to stop inputting marks: ")
    
    if user_input.lower().capitalize() == "Exit":
        loop = False
        break
    else: 
        mark = int(user_input)
        if 0 <= mark <= 100:
            #valid mark
            total_sum += mark
            counter += 1
        else: 
            print("Invalid mark.")

average = total_sum / counter 

print(f"Your average is: {average}")
