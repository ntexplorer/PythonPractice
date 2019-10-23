a = [(value**2 - 1) for value in range(0, 9)]
print(a)

b = [(value, (value**2)) for value in range(0, 9)]
print(b)

c = [(a[i] + b[i][0]) for i in range(len(a)) if (a[i] % 2 == 1)]
print(c)
l = ["   alpha   ", "beta\n\n     ", "    \n gamma \n"]
l1 = [w.strip() for w in l]
print(l1)
