from gestures import Gestures
from player import Player
import random

def computer_gesture(args):
    pass

def user_gesture(args):
    pass

class Game:
    def __init__(self):
        self.user_gesture = ''
        self.possible_gesture = ''
        self.computer_gesture = random
        # self.play_again = best of 3
        super.__init__()

    def game_actions(self):
        self.user_gesture = input("Enter a choice (rock[0], paper[1], scissors[2], lizard[3], spock[4]):")
        self.possible_gesture = ['rock[0]', 'paper[1]', 'scissors[2]', 'lizard[3]', 'spock[4]']
        self.computer_gesture = random(self.possible_gesture)

    print(f"(You chose {user_gesture}, computer chose {computer_gesture}.)")

    if user_gesture == computer_gesture:
        print(f"Both players selected {user_gesture}. It's a tie!")

    elif user_gesture == "rock[0]":
        if computer_gesture == ["scissors", "lizard"]:
            print("Rock crushes scissors! You win!")
    else:
        print("You lose!")

    elif user_gesture == "paper[1]":
        if: computer_gesture == ["rock", "spock"]:
     print("Paper covers rock! You win!")
    else:
    print("You lose!")

    elif user_gesture == "scissors":
    if computer_gesture == ["paper", "lizard"]:
           print("Scissors cuts paper! You win!")
    else:
       print("You lose!")

    elif user_gesture == 'lizard':
    if computer_gesture == ["spock", "paper"]:
     print("Lizard poisons Spock! You win!")
    else:
     print("You lose!")

    elif user_gesture == "spock":
       if computer_gesture == ["rock", "scissors"]:
    print("Spock vaporizes rock! You win!")
    else:
        print("You lose!")

def redemption(play_again):
        play_again = input("Play again? (yes/no): ")
        if play_again.lower() != "yes":
          print("Nice game!")


# Rock crushes Scissors
# Scissors cuts Paper
# Paper covers Rock
# Rock crushes Lizard
# Lizard poisons Spock
# Spock smashes Scissors
# Scissors decapitates Lizard
# Lizard eats Paper
# Paper disproves Spock
# Spock vaporizes Rock
