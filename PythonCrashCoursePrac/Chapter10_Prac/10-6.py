try:
    a = int(input("Please enter a number: "))
except ValueError:
    # except XXError should not come with ()
    print("The content you entered was not a number!")
else:
    try:
        b = int(input("Please enter another number: "))
    except ValueError:
        print("The content you entered was not a number!")
    else:
        print(a + b)
