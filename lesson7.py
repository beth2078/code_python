#Create a program that simulates the ability check from "Baldur's Gate 3"
#Shows how to use a randrange function*******

#0. Import
from random import randrange 

#1. Imput
difficulty = int(input("Enter the DC: "))

#2. Processing & Output
player_roll = randrange(1,21) 
#randrange(a,b) never includes b; mroeover, it goes up to b

print(f"The player has roled {player_roll} on their D20.")

if player_roll >= difficulty:
    print(f"The player was successfull as {player_roll} >= {difficulty}")
else: 
    print(f"The player was not successfull as {player_roll} <= {difficulty}")