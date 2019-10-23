# a)
d = {"Tom": 500, "Stuart": 1000, "Bob": 55, "Dave": 21274}
print(len(d))
print(d.keys())
print(d.values())
# b)
del d["Bob"]
d["Phil"] = 55
print(d)

# c)
def detect(a):
    if a in d:
        print("Yes")
    else:
        print("Not {}".format(a))
detect("Dave")
detect("Peter")
detect(500)

# d
for key, value in d.items():
    print(key, value)
for i in d:
    print(i)
