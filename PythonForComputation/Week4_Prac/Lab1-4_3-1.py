# 1
s = "structure"
dic = {}
for i in range(len(s)):
    dic[s[i]] = i
print(dic)
print("\n########################\n")
# 2
listA = list(range(11, 100, 11))
listB = list(range(1, 10))
listC = [(listA[i], listB[i]) for i in range(9)]
dicB = dict(listC)
print(dicB)
print("\n########################\n")
# 3
for a, b in dicB.items():
    print(a, b, end=" # ")
print()
print("\n########################\n")

# 3-1
for k in dicB:
    if (k + 11) in dicB:
        dicB[k] += dicB[(k + 11)]
print(dicB)
print("\n########################\n")

# 3-1_2
info = "Jack: Ben, 3, Cardiff;Jill: Sara, five, Bath"
records = info.split(';')
adic = {}
for item in records:
    str1, str2 = item.split(':')
    alist = str2.split(',')
    adic[str1.strip()] = tuple([x.strip() for x in alist])
print(adic)

# 3-1_3
with open('test.txt', 'w') as f:
    sts = "Python for Data Analysis.".split()
    for st in sts:
        f.write(st + "\n")
with open('test.txt', 'r')as f:
    st = f.read()
    print(st)
