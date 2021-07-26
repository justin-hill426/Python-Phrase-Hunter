# Create your Phrase class logic here.
class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def __str__(self):
        return self.phrase

    def __iter__(self):
        yield from self.phrase

    def display(self, guesses):
        """Displays the phrase on screen to the user"""
        for letter in self.phrase:
            if letter in guesses:
                print(f"{letter}", end=" ")
            else:
                print("_", end=" ")
        print()

    def check_complete(self, guesses):
        """Checks to see if the phrase has been completely guessed"""
        for letter in self.phrase:
            if letter not in guesses:
                return False
        return True
