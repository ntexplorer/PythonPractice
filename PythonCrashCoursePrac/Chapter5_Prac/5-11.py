number = [value for value in range(1, 10)]
for num in number:
    if num == 1:
        print("{}st".format(num))
    elif num == 2:
        print("{}nd".format(num))
    elif num == 3:
        print("{}rd".format(num))
    else:
        print("{}th".format(num))
