# Import your Game class
from game import Game
from phrase import Phrase
# Create your Dunder Main statement.
if __name__ == '__main__':
    new_game = Game()
    print(new_game.active_phrase)


# Inside Dunder Main:
## Create an instance of your Game class
## Start your game by calling the instance method that starts the game loop
