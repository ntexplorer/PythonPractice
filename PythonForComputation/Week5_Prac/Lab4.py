# try:
#     print(1/0)
# except ZeroDivisionError as e:
#     print("Error Code:" , e)

with open("input.txt") as f:
    first_line = f.readline()
    inputs = [f.readline().split() for x in range(int(first_line))]

for a, b in inputs:
    try:
        print(int(a) / int(b))
    except (ValueError, ZeroDivisionError) as e:
        print("Error Code: {}".format(e))

print("************")
print(first_line)
print(inputs)
