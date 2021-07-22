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
                         "To thine own self be true"]

    def __init__(self):
        self.missed = 0
        self.phrases = self.create_phrases()
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]

    def create_phrases(self):
        """Create a list of phrases for the game to be played"""
        list_of_phrases = []
        for phrase in self.POTENTIAL_PHRASES:
            list_of_phrases.append(Phrase(phrase))
        return list_of_phrases

    def get_random_phrase(self):
        """Return a random phrase from the list of phrases"""
        return random.choice(self.phrases)
