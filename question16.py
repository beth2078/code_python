"""
Queen’s University asked you to create an automatic open and 
close timer for their doors. The register office opens at 9:00am 
in the morning and closes at 18:30(6:30pm).

Inputs Specifications Assumption (2 Inputs)
1st Input → Hour (Integer) (0 <= Hour <= 23) 
2nd Input → Minute (Integer) (0 <= Minute <= 59)

Output:
Open
Closed

"""

# input
minutes = int(input())
hour = int(input())

# processing & output
if hour >= 0 and hour <= 23 and minutes >= 0 and minutes <= 59:
    print("step 1")
    if hour < 9 and hour > 18:
        print("step 2")
        if hour == 18 and minute >= 30:
            print("step 3")
            print("Closed.")
    elif hour >= 9 and hour <= 18:
        print("step 4")
        print("Open.")
    else:
        print("wut")
else:
    print("Invalid.")

