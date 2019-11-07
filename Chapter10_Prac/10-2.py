file_name = "learning_python.txt"

with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    # Code below is wrong
    # line.replace("Python", "C")
    # return line
    # can't use return in a loop
    print(line.replace("Python", "C").strip())

with open(file_name) as file_object:
    lines = file_object.read()
    print(lines.replace("Python", 'C'))
# It works


with open(file_name) as file_object:
    for line in file_object:
        print(line.replace("Python", "C").strip())
# It works too
