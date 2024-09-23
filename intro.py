first_name = input("Enter your first name here: ")
last_name = input("Enter your last name: ")
birth_year = int(input("Enter your birth year: "))
age = 2024 - birth_year
message = f"Hello {first_name} {last_name}.\nYou are {age} years old."
print(message)
if age >= 19:
    print("You can drink in Ontario, CAN\n")
else:
    print("You cannot drink in Ontario, CAN\n")