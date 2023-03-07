import random

# Define possible choices
options = ["rock", "paper", "scissors"]

# Define win-lose scenarios
win_scenarios = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

# Get player's choice
player_choice = input("Choose rock, paper, or scissors: ").lower()

# Make sure the player's choice is valid
while player_choice not in options:
    player_choice = input(
        "Invalid choice. Choose rock, paper, or scissors: ").lower()

# Get computer's choice
computer_choice = random.choice(options)

# Determine the outcome
if player_choice == computer_choice:
    print(f"Both players chose {player_choice}. It's a tie!")
elif win_scenarios[player_choice] == computer_choice:
    print(f"{player_choice} beats {computer_choice}. You win!")
else:
    print(f"{computer_choice} beats {player_choice}. You lose!")
