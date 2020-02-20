for value in range(1, 21):
    print(value)

number = [value for value in range(1, 21)]
for value1 in number:
    print(value1)
print(number)
print("\n")

number2 = [value for value in range(1, 1000001)]
a = min(number2)
b = max(number2)
print(a, b)
c = sum(number2)
print(c)
print("\n")

for value in range(1, 20, 2):
    print(value)
print("\n")

number3 = [value for value in range(3, 31, 3)]
for value in number3:
    print(value)
print("\n")

number4 = [value ** 3 for value in range(1, 11)]
for const in number4:
    print(const)
print(number4)
