'''
find_user("Colt", "Steele") # 1
find_user("Alan", "Turing") # 3
find_user("Not", "Here") # 'Not Here not found.'
'''

import csv


def find_user(first, last):
    with open("users.csv") as file:
        csv_reader = list(csv.DictReader(file))
        for (i, row) in enumerate(csv_reader, start=1):
            if (row["First Name"] == first) and (row["Last Name"] == last):
                return i
        return "{} {} not found.".format(first, last)


print(find_user("Grace", "Hopper"))
