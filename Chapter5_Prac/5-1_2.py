print("Test1 begin:")
str1 = input("Please enter string 1:")
str2 = input("Please enter string 2:")
if str1 == str2:
    print("Congradulations, these two strings match.")
else:
    print("Sorry, they don't match.")

print('\nTest2 begin:')
str3 = input("Please enter string 3:")
str4 = input("Please enter string 4:")
if str3.lower() == str4.lower():
    print("The lower style of these two strings matches.")
else:
    print("Sorry, the lower style of these strings don't match.")

print('\nTest3 begin:')
a = input("Please enter a number:")
b = input("Please enter another number:")
if int(a) > int(b):
    print(a+ " is larger than " + b)
elif int(a) == int(b):
    print(a + " equals " + b)
else:
    print(a + " is smaller than " + b)

print('\nTest4 begin:')
a = input("Please enter 123:")
b = input("Please enter 321:")
if int(a) == 123 and int(b) == 321:
    print("a is 123 and b is 321")
else:
    print("At least one of them is not correct.")
if int(a) == 123 or int(b) ==321:
    print('\nAt least one of them is correct.')
else:
    print('Both of them are incorrect.')

print('\nTest5 begin:')
item = input('Please enter an item:')
item_list = ["cup", "glasses", "box", "toy"]
if item in item_list:
    print("The item you choose is in the list.")
else:
    print("The list does not contain the item you chose.")
if item not in item_list:
    print("The item you choose is out.")
else:
    print("It is still for sale!")
