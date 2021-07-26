from game import Game


def play_again():
    """Solicits a y or n from the user to see if the user would like to play again"""
    user_input = ""
    while user_input != "y" and user_input != "n":
        try:
            user_input = input("Would you like to play again? (y/n)").lower()
            if len(user_input) > 1:
                raise ValueError()
            elif user_input != "y" and user_input != "n":
                raise ValueError("Please enter y (Yes) or n (No): ")
        except ValueError as err:
            print("Please enter y (Yes) or n (No)")
    return user_input == 'y'


def goodbye():
    """Prints a goodbye message to the user to end the program"""
    print("\t\t\t\t\t============================")
    print("\t\tThank You for playing Shakespeare's version of Phrase Hunter!"
          "\n\t\tWilliam Shakespeare was an English playwright, poet, and actor, "
          "\n\t\twidely regarded as the greatest writer in the English language")
    print("\t\t\t\t\t============================")


if __name__ == '__main__':
    while True:
        new_game = Game()
        new_game.start()
        if not play_again():
            break
    goodbye()
