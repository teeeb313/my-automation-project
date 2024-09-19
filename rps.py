import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS =3
    
print (RPS(2))


print("")
playerchoice = input("Enter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

# Convert the player's choice to an integer
try:
    player = int(playerchoice)
except ValueError:
    sys.exit("You must enter a valid number: 1, 2, or 3.")

# Check if the player's input is within the valid range
if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3.")

# Computer randomly chooses 1, 2, or 3
computer = random.choice([1, 2, 3])  # Renamed computerchoice to computer for consistency

print("")
print(f"You chose {playerchoice}.")
print(f"Python chose {computer}.")  # Updated to use the correct variable
print("")

# Game logic
if player == 1 and computer == 3:
    print("You Win!")
elif player == 2 and computer == 1:
    print("You Win!")
elif player == 3 and computer == 2:
    print("You Win!")
elif player == computer:
    print("TIE GAME!")
else:
    print("Python won!")
    
    
    
    
   