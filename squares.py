#0. import statements
from math import sqrt, floor 
# Best to use from (if you don't want to use the whole module) 

#1. input
tiles = int(input("Enter a number of tiles: "))

answer = floor(sqrt(tiles))

#2. processings
print(f"The largest square had a single side length of {answer}.")
