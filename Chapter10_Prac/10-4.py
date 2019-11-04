trigger = True
while trigger:
    print("Enter 'q' to quit.")
    name = input("Please enter your name: ")
    if name != "q":
        print("Hello, {}".format(name.title()))
        with open("guest_book.txt", "a") as guest_book:
            guest_book.write(name + "\n")
    else:
        print("Input terminated!")
        break
