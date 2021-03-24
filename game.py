from gestures import Gestures
from player import Player

class Game:
    def __init__(self):
        self.user_gesture = ''
        self.possible_gesture = ''
        self.computer_gesture = ''
        super.__init__(self)

def player_actions(player, computer, user_action):
    user_gesture = input("Enter a choice (rock, paper, scissors, lizard, spock): ")
    possible_gesture = ["rock", "paper", "scissors, lizard, spock"]
    computer_gesture = random.choice(possible_gesture)
    print(f"(You chose {user_action}, computer chose {computer_gesture}.)")

    if user_gesture == computer_gesture:
     print(f"Both players selected {user_action}. It's a tie!")

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


    elif user_gesture == "rock":
      if computer_gesture == "scissors":
        print("Rock crushes scissors! You win!")
    else:
        print("You lose!")

    elif user_gesture == "paper":
        if computer_gesture == "rock":
        print("Paper covers rock! You win!")
    else:
    print("You lose!")

    elif user_gesture == "scissors":
        if computer_gesture == "paper":
      print("Scissors cuts paper! You win!")
    else:
     print("You lose!")

    elif user_gesture == "lizard":
        if computer_gesture == "spock":
     print("Lizard poisons Spock! You win!")
    else:
     print("You lose!")

    elif user_gesture == "spock":
        if computer_gesture == "rock":
        print("Spock vaporizes rock! You win!")
     else:
         print("You lose!")