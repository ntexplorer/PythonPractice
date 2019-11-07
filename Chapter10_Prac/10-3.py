name = input("Please enter your name: ")

with open("guest.txt", 'a') as file_name:
    file_name.write(name)
