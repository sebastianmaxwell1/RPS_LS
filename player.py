from game import Game
from gestures import Gestures


class Player:

    def __init__(self, user_player, computer_player):
        super().__init__(Game)
        self.name = input("Please enter your name")
        self.move = user_player
        self.computer_move = computer_player
        self.gesture_list = ['rock[0]', 'paper[1]', 'scissors[2]', 'lizard[3]', 'spock[4]']
        self.computer_gesture_list = ['rock[0]', 'paper[1]', 'scissors[2]', 'lizard[3]', 'spock[4]']

    def user_move(self):
        self.move = self.gesture_list

    def computer_move(self, computer_player):
        self.computer_move = self.computer_gesture_list
