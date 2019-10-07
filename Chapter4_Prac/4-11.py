my_items = ["cup", "glasses", "box", "toy"]
friend_items = my_items[:]
my_items.append("shoes")
friend_items.append("brush")
print("My items are:\n")
for my_item in my_items:
    print(my_item.title())
print("My friend's items are:\n")
for friend_item in friend_items:
    print(friend_item.title())
