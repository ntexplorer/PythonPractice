import random
import game

class GuessNumberGame(game.Game): #subclass of Game
    '''
    Guess My Number Game -- A Game in which the player provides a number and the computer guess it.
    '''
    def __init__(self, attempts):
        super(GuessNumberGame, self).__init__(attempts)
        self.greeting = "You, the player, are thinking of a number between 1 and 100.\n\
I, the clever computer will try to guess it in as few \n\
attempts as possible. I have {} attempts.".format(self.attempts)


    def play(self):
        pass         #to be completed
