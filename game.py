
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

LETTER_TO_COLOR = {color[0]:color for color in COLORS}

NUM_GUESSES = 10


class Game(object):
    def __init__(self, code=None):
        self.code = self.make_code() if code is None else code
        self.guesses_remaining = NUM_GUESSES

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

    def clean_guess(self, guess):
        output = [LETTER_TO_COLOR[letter] for letter in guess.lower() if letter in LETTER_TO_COLOR]
        return output if len(output) == len(self.code) else None

    def solicit_guess(self):
        clean_guess = None
        while clean_guess == None:
            index = NUM_GUESSES - self.guesses_remaining + 1
            msg = (f'{index}. Next guess '
                   f'(available colors: R, O, Y, G, B, P - format RROY):\n\n> ')
            guess = input(msg)
            clean_guess = self.clean_guess(guess)
            if clean_guess == None:
                print('\nInvalid input, please try again')

        exact_matches, color_matches = self.evaluate_guess(clean_guess)
        if exact_matches == len(self.code):
            print('\nCongratulations! You guessed right!!')
            return True

        self.guesses_remaining -= 1

        msg = (
            # f'>\n'
            f'> '
            f'{exact_matches} exact match{_ess(exact_matches, "es")}. '
            f'{color_matches} wrong position match{_ess(color_matches, "es")}. '
            f'{self.guesses_remaining} '
            f'guess{_ess(self.guesses_remaining, "es")} remaining.'
            f'\n'
        )
        print(msg)

        return self.guesses_remaining < 0

    def play(self):
        while not self.solicit_guess():
            pass

def _ess(val, plural_suffix, single_suffix=''):
    return single_suffix if val == 1 else plural_suffix


##

def test():
    g1 = Game([RED, RED, YELLOW, YELLOW])
    print(g1.evaluate_guess([RED, RED, YELLOW, YELLOW]) == (4,0))
    print(g1.evaluate_guess([YELLOW, YELLOW, RED, RED]) == (0,4))

def main():
    game = Game()
    game.play()

if __name__ == '__main__':
    import sys
    if '-t' in sys.argv or '--test' in sys.argv:
        test()
    else:
        main()
