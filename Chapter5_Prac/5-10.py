current_user = ["Alex", "Mary", "Jack", "Bob", "Larry"]
new_user = ["Mary", "Ams", "Linc", "Poler", "Bob"]
for user in new_user:
    if user in current_user:
        print("This user name '{}' has already been used.".format(user))
    else:
        print("User name '{}' available.".format(user))
