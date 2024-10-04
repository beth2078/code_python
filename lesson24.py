# Longest Name Finder

# solution
# variable initalizations

name = ' '
longest_length = 0
longest_name = ' '

while name != 'X':
    name = input("Enter your name or 'X' to exit: ").upper()
    current_length = len(name)
    # if current_length > longest_length and name != "x":
    #     longest_length = current_length
    #     longest_name = name

    if name != 'X':
        if current_length > longest_length:
            longest_length = current_length
            longest_name = name
        # end of if 
    else: 
        print("End the inputs.")
# end while loop

if longest_name:
    print(f'The longest name with {longest_length} characters is  {longest_name}.')
else:
    print("Not enough data.")
