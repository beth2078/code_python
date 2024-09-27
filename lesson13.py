#Special Day

#1. input
month = int(input())
day = int(input())

#2. processing & output
if month == 2 and day == 18:
    print("Special.")
else:
    if month < 2:
        print("Before.")
    elif month > 2:
        print("After.")
    else:
        # in the month of Feb
        if day < 18:
            print("Before.")
        else: 
            print("After.")