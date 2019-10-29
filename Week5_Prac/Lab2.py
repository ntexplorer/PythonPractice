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

import shelve
print("Shelving Lists...")
shelf = shelve.open("s_week5.dat")

shelf['lista'] = lista
shelf['listb'] = listb
shelf['listc'] = listc

shelf.sync()
shelf.close()
print("Success.")

print("Retrieving Lists from Shelf...")
shelf = shelve.open('s_week5.dat')

print('List a: {}'.format(shelf['lista']))
print('List b: {}'.format(shelf['listb']))
print('List c: {}'.format(shelf['listc']))
shelf.close()
