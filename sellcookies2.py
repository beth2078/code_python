#1. Input 
starting_money = float(input("How much money do you have? "))
cookies_sold = input("How many cookies did you sell? ") 

# #2. Processing 
# big_cookies = 0 #example of initializing 
# cookies = 0
big_cookies = cookies_sold.count('b')
cookies = cookies_sold.count('c')


# for current_cookie in cookies_sold:
#     if current_cookie == "c":
#         cookies += 1

#     elif current_cookie == "b":
#         big_cookies+= 1 
#     else:
#         print(f"{current_cookie} is not a valid sale item.")
# #end of for loop 

total_cookies = big_cookies + cookies
profit = (big_cookies * 1.25) + (cookies * 0.75)
end_day = starting_money + profit
print(f"We sold {total_cookies} cookies.\nWe made ${profit}\nWe now have ${end_day}")