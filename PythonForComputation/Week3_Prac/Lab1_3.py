import random
import string

target_number = random.choice(string.ascii_lowercase)
print('Guess the letter in lowercase: ')
guess = ""
while guess != target_number:
    guess = input('Please meake your guess: ')
    if ord(guess) < ord(target_number):
        print("The target letter is higher!")
    elif ord(guess) > ord(target_number):
        print("The target letter is lower!")
    else:
        print("Bingo!")
        break
