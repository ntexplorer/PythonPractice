import random
the_word = input("Please enter a word: ")
#word = the_word
#jumble = ""
#while len(word) > 0:
#    a = random.choice(word)
#    jumble += a
#    word = word.replace(a, '')
#print("The jumble of the word is: " + jumble)
new = random.sample(list(the_word), len(the_word))
final = []
for i in new:
    final.append(i)
print("".join(final))
