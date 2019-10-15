def show_magicians(magicianName):
    for magician in magicianName:
        print(magician.title())

def make_great(greatName):
    newList = []
    while greatName:
        for names in greatName:
            newName = "the Great " + greatName.pop()
            newList.append(newName)
    return newList

magician_Name = ['David Jones', 'Qian Liu', "John Doe"]
show_magicians(make_great(magician_Name[:]))
print(magician_Name)
