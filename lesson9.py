#Rock Paper Scissors Game
#player vs. AI

#0. Import
from random import choice

#1. Input
invalid = True
player = '' #variable init 

while invalid: 
    #code block for the while loop starts here
    player = input("Enter a choice of rock, paper, or scissors: ")

    #if the player spelt the rock paper or scissors incorrectly the code will keep asking
    if player in {'rock', 'paper', 'scissors'}:
        # we use in operator in python often with sets because of its faster excececution speed
        invalid = False 
# end of while loop

#2. Processing 
cpu = choice(['rock', 'paper', 'scissors'])
print(f"The CPU chose {cpu}.")
#3. Game logic starts here
if player == cpu:
    print("Tie Game.")
else:
    #Guarenteed that one player has won the game
    #Nesting (if statement within an if statement)
    if player == 'rock':
        if cpu == 'paper':
            print("The CPU has won the game.")
        else: 
            print("The Player has won the game.")
    elif player == 'scissors':
        if cpu == 'paper':
            print("The CPU has won the game.")
        else: 
            print("The Player has won the game.")
    else:
    # player chose scissors
        if cpu == 'rock':
            print("The CPU has won the game.")
        else: 
            print("The Player has won the game.")
#end of game logic
