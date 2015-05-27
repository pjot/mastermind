import random

class Mastermind:
    CORRECT_PLACEMENT = "1"
    CORRECT_COLOR = "0"
    ALLOWED = ["1", "2", "3", "4", "5", "6"]

    board = []
    result = []

    def run(self):
        self.create_board()
        while True:
            guess = raw_input("Guess (1-6): ")
            while not self.validate_guess(guess):
                guess = raw_input("Guess again: ")
            if self.is_correct(guess):
                print("You won: " +  guess)
                exit()
            self.print_result()

    def validate_guess(self, guess):
        guess = guess.strip()
        if len(guess) != 4:
            return False
        for char in guess:
            if not char in self.ALLOWED:
                return False
        return True

    def create_board(self):
        self.board = []
        for i in range(4):
            self.board.append(random.choice(self.ALLOWED))

    def is_correct(self, guess):
        guess = self.parse_guess(guess)
        if guess == self.board:
            return True

        remaining_guesses = list(guess)
        remaining_board = list(self.board)
        self.result = []
        for i, b in enumerate(self.board):
            if b == guess[i]:
                self.result.append(self.CORRECT_PLACEMENT)
                remaining_guesses.remove(b)
                remaining_board.remove(b)

        for g in remaining_guesses:
            if g in remaining_board:
                remaining_board.remove(g)
                self.result.append(self.CORRECT_COLOR)

        return False

    def print_result(self):
        print("".join(self.result))

    def parse_guess(self, guess):
        return list(l for l in guess)

mm = Mastermind()
mm.run()
