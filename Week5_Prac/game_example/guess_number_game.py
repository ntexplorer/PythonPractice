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

    #set the initial values
    def _getResponse(self, guess):
        response= input("Is it "+str(guess)+"(Yes, Higher, Lower)?")
        while(response!="Yes" and response!="Higher" and response!="Lower"):
            response= input("Please answer Yes, Higher or Lower: ")
        return response

        
    def play(self):
        #set the initial values
        the_number=int(input("Think of a number: "))
        low=1
        high=100

        guess=random.randint(1, 100)
        response = self._getResponse(guess)
        count = 1
        #guess loop
        while response != "Yes":
            if count>=self.attempts:
                break
            if(response == "Higher"): low=guess+1
            elif (response == "Lower"): high=guess-1
            guess = random.randint(low, high)     
            response= self._getResponse(guess)
            count += 1
            
        if response == "Yes":
            print ("I guesses it! the number was {}.".format(the_number))
            print ("It took me only {} attempts. See, how clever I am.".format( count))
        else:
            print("Arrgh, you beat me.")
