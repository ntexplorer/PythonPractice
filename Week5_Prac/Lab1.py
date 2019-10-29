lista = []
listb = []
listc = []

for i in range(1, 11):
    if i % 2 == 0:
        listb.append(i)
    else:
        lista.append(i)

for n in range(1,6):
    listc.append(n*5)

print(lista)
print(listb)
print(listc)

import pickle

print("Pickle lists")
f = open("p_week5.dat", "wb")
pickle.dump(lista, f)
pickle.dump(listb, f)
pickle.dump(listc, f)
f.close()

print("Unpickling Lists")

f = open("p_week5.dat", "rb")
a = pickle.load(f)
b = pickle.load(f)
c = pickle.load(f)

print(a)
print(b)
print(c)
f.close
