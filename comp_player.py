from player import Player
from gesture import Gesture
import random


class Computer(Player):

    def __init__(self):

        super().__init__()

    def pvp(self):

        print("Choose a gesture!")
        print(Gesture().gestures)
        self.choice_1 = int(input("Player One Enter Choice: "))
        while self.choice_1 != 0 and self.choice_1 != 1 and self.choice_1 != 2 and self.choice_1 != 3 and self.choice_1 != 4:
            print("Invalid input please try again")
            self.choice_1 = int(input("Player 1 chose: "))
        self.choice_2 = get_random_number(0, 4)
        print("")
        print(f"Player 1 chooses {Gesture().gestures[self.choice_1]}")
        print(f"Computer chooses {Gesture().gestures[self.choice_2]}")
        print("")
        return self.choice_1, self.choice_2


def random_number(min_value, max_value):
    return random.randint(min_value, max_value)


def get_random_number(num_1, num_2):
    random_int = random_number(num_1, num_2)
    return random_int