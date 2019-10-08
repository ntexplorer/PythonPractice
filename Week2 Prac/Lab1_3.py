seconds = int(input("Please enter the number of second:"))
def time_trans(a):
    return a // 3600, a % 3600 //60, a % 3600 % 60
i, j, k = time_trans(seconds)
print("You got " + str(seconds) + " seconds.\n Which equals to {} hours + {} minutes + {} seconds.".format(i, j, k))
