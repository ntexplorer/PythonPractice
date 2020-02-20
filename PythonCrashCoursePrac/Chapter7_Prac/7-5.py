message = "Check the price of the tickets by entering the age."
message += "\nEnter 'quit' to exit."
print(message)
while True:
    age = input("Please enter the age of the customer: ")
    if age.lower() != "quit" and age.isdigit() == True:
        if 0 < int(age) < 3:
            print("You can get a ticket for free!")
        elif 3 <= int(age) <= 12:
            print("The ticket costs $10.")
        elif int(age) > 12:
            print("The ticket costs $15.")
    elif age.isdigit() == False and age.lower() != "quit":
        print("Input Invalid!")
    else:
        break
