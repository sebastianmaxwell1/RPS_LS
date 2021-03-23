


class Gestures:

     def __init__(self,


def assigned_number_to_gesture(number):
        if number == 0:
            return "Rock"
        elif number == 1:
            return "Paper"
        elif number == 2:
            return "Scissors"
        elif number == 3:
            return "lizard"
        elif number == 4:
            return "Spock"
        else:
            print("Error,Enter a correct gesture")

            def assigned_gesture_to_number(name):
                if name == "Rock":
                    return 0
                elif name == "Paper":
                    return 1
                elif name == "Scissors":
                    return 2
                elif name == "lizard":
                    return 3
                elif name == "Spock":
                    return 4
                else:
                    print()
                    name + "is not a gesture in this game!"