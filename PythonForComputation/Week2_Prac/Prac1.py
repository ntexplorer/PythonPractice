import datetime

name = input("Please enter your name:")
age = input("Please enter your age:")
date = datetime.datetime.now()
year_of_100 = date.year + (100 - int(age))
print("Hi, " + name + ". You will turn 100 in " + str(year_of_100) + ".")
