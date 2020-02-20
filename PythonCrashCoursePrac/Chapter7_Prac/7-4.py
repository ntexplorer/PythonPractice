toppings1 = []
add_topping1 = ""
while True:
    add_topping1 = input("What kind of toppings do you want: ")
    if add_topping1 != "quit":
        toppings1.append(add_topping1.title())
        print("You have added {} in your pizza!".format(add_topping1.title()))
    else:
        break

print("\nThere comes the current topping list:")
for topping in toppings1:
    print("{}".format(topping))
