# Create your Game class logic in here.
import random
from phrase import Phrase


class Game:
    POTENTIAL_PHRASES = ["To be, or not to be: that is the question",
                         "Romeo, Romeo! Wherefore art thou Romeo",
                         "Beware the Ides of March",
                         "If music be the food of love play on",
                         "There are more things in heaven and earth, Horatio, than are dreamt of in your philosophy",
                         "Some are born great, some achieve greatness, and some have greatness thrust upon them",
                         "To thine own self be true",
                         "Love all, trust a few, do wrong to none"]

    def __init__(self):
        self.missed = 0
        self.phrases = self.create_phrases()
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" ", ",", "!", ".", ":"]

    def create_phrases(self):
        """Create a list of phrases for the game to be played"""
        list_of_phrases = []
        for phrase in self.POTENTIAL_PHRASES:
            list_of_phrases.append(Phrase(phrase))
        return list_of_phrases

    def get_random_phrase(self):
        """Return a random phrase from the list of phrases"""
        return random.choice(self.phrases)

    def welcome(self):
        """Prints a welcome message for the game"""
        print("\t\t\t\t\t============================")
        print("\t\t\tWelcome to Shakespeare's Phrase Hunter!"
              "\n\t\t\tYou will be tested on your Shakespeare knowledge with various "
              "\n\t\t\tphrases from his writings.")
        print("\t\t\t\t\t============================")

    def start(self):
        """Starts the game and controls user interactivity"""
        self.welcome()
        while self.missed < 5 and not self.active_phrase.check_complete(self.guesses):
            print(f"Number missed: {self.missed}")
            self.active_phrase.display(self.guesses)
            user_guess = self.get_guess()
            if user_guess == "INVALID":
                continue
            self.guesses.append(user_guess)
            if not self.check_guess(user_guess):
                print(f"Sorry, there are no {user_guess}'s in the phrase")
                self.missed += 1
            else:
                count_correct = self.active_phrase.phrase.count(user_guess)
                if count_correct == 1:
                    print(f"Great job! There is {count_correct} '{user_guess}' in the phrase")
                else:
                    print(f"Great job! There are {count_correct} {user_guess}'s in the phrase")
        self.game_over()

    def get_guess(self):
        """Gets a valid, lowercase character, guess from the user"""
        new_guess = ""
        try:
            new_guess = input("Enter a letter: ").lower()
            if len(new_guess) > 1:
                new_guess = "INVALID"
                raise ValueError("The guess you entered was too long. Make sure that it is only one character")
            elif len(new_guess) < 1:
                new_guess = "INVALID"
                raise ValueError("The guess you entered was too short. Make sure that it is only one character")
            elif ord(new_guess) < 97 or ord(new_guess) > 122:
                new_guess = "INVALID"
                raise ValueError("Your input was deemed invalid! Please make sure input is a character a-z")
            elif new_guess in self.guesses:
                print(f"You already guessed the letter {new_guess}, try again")
                new_guess = "INVALID"
        except ValueError as err:
            print(err)
        return new_guess

    def check_guess(self, user_guess):
        """Checks to see if the guess is in the active phrase"""
        return user_guess in self.active_phrase

    def game_over(self):
        """Prints a win/loss message for the outcome of the game"""
        if self.missed == 5:
            print("You Lost! Better Luck Next Time!")
        else:
            print("You Won! Congratulations!")
        self.print_full_phrase()

    def print_full_phrase(self):
        """Print the full, correct, phrase that was used for the game"""
        print("The phrase was...")
        print("\t", end="")
        for i in self.active_phrase:
            print("*", end="")
        print(f"\n\t{self.active_phrase}")
        print("\t", end="")
        for i in self.active_phrase:
            print("*", end="")
        print()


