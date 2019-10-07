magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!\n")

for value in range(1,5):
    print(value)
numbers = list(range(1,10))
print(numbers)

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

message = "\tHello World!"
print(message.strip())
