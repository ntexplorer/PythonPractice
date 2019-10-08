for char in "1bc4":
    print(char)
    print(type(char))

str1 = input("\nPlease input a string: ")
for i in str1:
    print(not i.isdigit())
for i in str1:
    if not i.isdigit() == True:
        print(i.upper())
    else:
        print("Not a letter.")
