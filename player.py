from game import Game
from gestures import Gestures


class Player:

    def __init__(self, user_player, computer_player):
        super().__init__()
        self.name = input("Please enter your name")
        self.move = ''
        self.user_gesture_list = ['rock', 'paper', 'scissors', 'lizard', 'spock']

    def set_move(self):
        self.move = self.user_gesture_list['rock', 'paper', 'scissors', 'lizard', 'spock']
