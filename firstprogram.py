#Basic calulator

#Custom functions
def numericInput(prompt):
    while True:
        value = input(prompt)
        try: 
            value = float(value)
            return value
        except: 
            print(f"{value} can't be converted into a floating point.")
#end of numeric input

#User menu 
def menu():
    menu = """
Calculator Menu Options:
    1. Add (+)
    2. Subtract (-)
    3. Multipy (*)
    4. Divide (/)
    5. Exit Program (Exit)

"""
    while True: 
        print(menu)
        user_choice = input("User's Choice: ").lower() 
        #.lower() puts the result of the input into lower case
        if user_choice in {'add', '1', '+'}:
            return 1
        elif user_choice in {'subtract', '2', '-'}:
            return 2
        elif user_choice in {'multiply', '3', '*'}:
            return 3
        elif user_choice in {'divide', '4', '/'}:
            return 4
        elif user_choice in {'exit', '5'}:
            return 5
        else:
            print(f"{user_choice} is not a menu option!")

while True: 
    #Main part of program starts here:
    #1. Run menu 
    menu_result = menu()

    #2. User chooses numbers
    num1 = numericInput("Enter a number: ")
    num2 = numericInput("Enter another number: ")

    #3. Use user choices to exicute the calculation
    if menu_result == 1:
        #addition
        answer = num1 + num2
        print(f"{num1} + {num2} = {answer}")
    elif menu_result == 2:
        #subtraction
        answer = num1 - num2
        print(f"{num1} - {num2} = {answer}")
    elif menu_result == 3:
        #multiplication
        answer = num1 * num2
        print(f"{num1} * {num2} = {answer}")
    elif menu_result == 4:
        #division
        #fixing 0 division problem
        try: 
            answer = num1 / num2
            print(f"{num1} / {num2} = {answer}")
        except ZeroDivisionError:
            print("You cannot divide by 0. Try different numbers")

    elif menu_result == 5:
        #exiting code
        print("Thank you for using the calculator!")
        #exit infinite loop
        break
