a = ['football', 'rugby', 'hockey', 'tennis']
print(a[0])
print(a[-1])
a.append("cycling")
print(a)
print(len(a))

for i in a:
    print(i[0])

del a[0]
print(a)

b = a[1:3]
print(b)
