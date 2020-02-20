place = ""
name = ""
answer_sheet = {}
question_active = True
while question_active:
    name = input("Please enter your name: ")
    place = input("If you could visit one place in the world, where would you go? ")
    answer_sheet[name] = place

    again = input("Would you like to let others answer the question?(yes/no)")
    if again != "no":
        continue
    else:
        break
for name, place in answer_sheet.items():
    print("\t{} wants to visit {} if he/she got a chance.".format(name.title(), place.title()))
