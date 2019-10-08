import random
def jumble(words):
    new_words = words.split(" ")
    out = ''
    for word in new_words:
        if word.istitle():
            out = out + " " + "".join(random.sample(list(word), len(word))).title()
        elif  ("!" in word) or ("," in word) or ("." in word):
            out = out + " " + "".join(random.sample(list(word)[:-1], len(word) - 1)) + word[-1]
        else:
            out = out + " " + "".join(random.sample(list(word), len(word)))
    print(out.lstrip())
sentence = input("Please enter a sentence: ")
jumble(sentence)
