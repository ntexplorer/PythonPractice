a = list(range(10))
print(a)
print(a[2])
#print(a[10])
print(a[-3])
print(a[0:3])
print(a[:3])
print(a[4:])
print(a[:])
print(a[::2])
print(a[5::-1])
print(a[::2][3])
#doesn't count right, count left
print("##############")
print(a[4])
print(a[-6])
print(a[0:2])
print(a[:3])
print(a[-2:])
print(a[::3])
print(a[::-3])
print("##############")
print(a[::2])
print(a[::-1])
print(a[-1::-2])
print(a[-1:-5:-2])
print("##############")
a = list(range(10))
a[0] = 10
print(a)

print("##############")
a = list(range(10))
a[2:4] = ['a', 'b']
print(a)
print("##############")
a = list(range(10))
a[2:4] = ['a', 'b', 'c', 'd']
print(a)
'''print("##############")
a = list(range(10))
a[2:4:2] = ["a", "b"]
print(a)'''
print("##############")
a = list(range(10))
a[2:6:2] = ["a", "b"]
print(a)
print("##############")
a = list(range(10))
del a[0:2]
print(a)
print("##############")
a = list(range(10))
del a[::2]
print(a)
print("##############")
a = list(range(10))
a[1::2] = a[::-2]
print(a)
