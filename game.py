
# Colors:
# R, O, Y, G, B, P
#
# Computer picks permutation of 4 (can repeat colors)
#
# Player makes guesses each time of a permutation of 4
#
# For each guess, computer shows:
#
# *   black pegs for # correct color and position
# *   white pegs for # correct color and wrong position
#

RED = 'red'
ORANGE = 'orange'
YELLOW = 'yellow'
GREEN = 'green'
BLUE = 'blue'
PURPLE = 'purple'

COLORS = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]

class Game(object):
    def __init__(self):
        self.code = self.make_code()
        self.guesses_remaining = 10

    def make_code(self):
        # TODO - fill out
        return [RED, ORANGE, YELLOW, GREEN]

    def evaluate_guess(self, guess):
        """
        guess - list<color> - a guess to match self.code
        """
        assert len(guess) == len(self.code), 'guess and code do not match len'
        assert all(color in COLORS for color in guess), 'bad colors given in guess'

        remaining_guess = []
        remaining_code = []

        exact_matches = 0
        color_matches = 0

        # check for exact matches
        for i, (guess_color, code_color) in enumerate(zip(guess, self.code)):
            if guess_color == code_color:
                exact_matches += 1
            else:
                remaining_guess.append(guess_color)
                remaining_code.append(code_color)

        # check for correct color, wrong location
        for guess_color in remaining_guess:
            if guess_color in remaining_code:
                remaining_code.remove(guess_color)
                color_matches += 1

        return exact_matches, color_matches
