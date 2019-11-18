import re

x = 10
print(f"This is great\tLet's go,{x}")

print(r"\n\d")

text = '''John and Jane went to Coffee #1 on 140 Queen Street. They had coffees that cost a total of č5.20 and then waited for a couple of friends. They hadn't seen each other for over 6 years. Both of them have a sweet tooth so they also spend almost č20 on cakes in a shop at 30 Castle Street.'''

print(text)

# numbers = []
# for c in text:
#     if c.isnumeric():
#         numbers.append(int(c))
# print(numbers)

# numbers = []
# nr = ''
# for c in text:
#     if c.isnumeric():
#         nr += c
#     else:
#         if nr != '':
#             numbers.append(float(nr))
#             nr = ''
# print(numbers)

print(re.findall(r'\d+', text))
