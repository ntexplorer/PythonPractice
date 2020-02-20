user_list = ["Admin", "Alice"]
if not user_list:
    print("We need to find some users!")
else:
    for user in user_list:
        if user == user_list[1]:
            print("Hello {}, would you like to see a status report?".format(user_list[1]))
        else:
            print("Hello {}, thank you for logging in again.".format(user))
