import random

import game


class GuessNumberGame(game.Game):  # subclass of Game
    '''
    Guess My Number Game -- A Game in which the player provides a number and the computer guess it.
    '''

    def __init__(self, attempts):
        super(GuessNumberGame, self).__init__(attempts)
        self.greeting = "You, the player, are thinking of a number between 1 and 100.\n\
I, the clever computer will try to guess it in as few \n\
attempts as possible. I have {} attempts.".format(self.attempts)
        self.num = 0
        self.guess = 0
        self.answer = ""
        self.low = 1
        self.high = 100
        self.count = 1

    def get_response(self):
        self.answer = input("Is it {}(Yes, Higher, Lower)? ".format(self.guess))
        while (self.answer.title() != "Yes" and self.answer.title() != "Higher" and self.answer.title() != "Lower"):
            self.answer = input("Please enter 'Yes' 'Higher' or 'Lower': ")
        return self.answer

    def play(self):
        self.num = int(input("Think of a number: "))
        while self.answer.title() != "Yes":
            self.guess = random.randint(self.low, self.high)
            response = self.get_response()
            if self.count < self.attempts:
                self.count += 1
                if self.answer.title() == "Higher":
                    self.low = self.guess + 1
                elif self.answer.title() == "Lower":
                    self.high = self.guess - 1
            else:
                break

        if self.answer.title() == "Yes":
            print("I guesses it! the number was {}.".format(str(self.num)))
            print("It took me only {} attempts. See, how clever I am.".format(str(self.count)))
        else:
            print("Arrgh, you beat me.")
