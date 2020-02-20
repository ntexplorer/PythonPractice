file_name = "learning_python.txt"

with open(file_name) as file_object:
    contents = file_object.read()
    print(contents.strip())
    print("####################")

with open(file_name) as file_object:
    for line in file_object:
        print(line.strip())
    print("####################")

with open(file_name) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
print("####################")
