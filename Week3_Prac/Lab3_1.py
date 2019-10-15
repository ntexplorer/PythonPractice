def list_compare(a, b):
    newA = list(a)
    newB = list(b)
    lastA = []
    lastB = []
    c = []
    while newA != []:
        for n in newA:
            popA = newA.pop()
            if popA not in lastA:
                lastA.append(popA)
    while newB != []:
        for n in newB:
            popB = newB.pop()
            if popB not in lastB:
                lastB.append(popB)
    for i in lastA:
        if i in lastB:
            c.append(i)
    return c

a = (2, 3, 4, 5, 6, 7, 8, 3, 4)
b = (10, 4, 6, 6, 12, 2, 7)
print(list_compare(a, b))
