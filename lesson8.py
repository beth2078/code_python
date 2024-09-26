#Tournament Selection

#1. Input
#this is assuming the game results with either be a win or a loss
win_counter = 0
for i in range(6): 
#range of 6 --> 0,1,2,3,4,5 in computer memory
    current_result = input(f"Enter the game {i+1} result: ")
    if current_result == "W":
        win_counter += 1 # win_counter = win_counter + 1
# end of for loop

#2. Processing
group = 0 #good happit to do before changing value in a for or while loop
if win_counter > 4:
    group = 1
elif win_counter > 2: 
    group = 2
elif win_counter > 0:
    group = 3

if group == 0:
    print("The player is eliminated")
else:
    print(f"The player is placed in group {group}.")

