def age_fb(age):
    age = int(input("Please enter the age of the people: "))
    if age < 2:
        print("It's a baby!")
    elif 2 <= age < 4:
        print("He's learning how to walk!")
    elif 4 <= age < 13:
        print("He's a child.")
    elif 13 <= age < 20:
        print("He's a teenager.")
    elif 20 <= age < 65:
        print("He's an adult.")
    else:
        print("He's an old man.")


age_fb(input())
