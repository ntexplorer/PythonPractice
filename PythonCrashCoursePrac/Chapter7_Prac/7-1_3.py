car = input('What kind of car do you want: ')
print('Let me see if I can fidn you a {}...'.format(car))

guest_num = input('How many people are coming? ')
if int(guest_num) >= 8:
    print("Sorry, we don't have enough table...")
elif 0 < int(guest_num) < 8:
    print("Good, we have enough tables for you to come!")
else:
    print("Unreadable input :(")

num = int(input("Please enter a number: "))
if num % 10 == 0:
    print("It can be done by 10.")
else:
    print('Sorry.')
