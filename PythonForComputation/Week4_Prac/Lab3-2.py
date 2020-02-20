ids = ('a', "b", 'c', 'd', 'e', 'f')
mywords = ('Tim', 'Sara', 'flew', 'space', 'pair', 'slippers')

d = {}
for i in range(len(ids)):
    d[ids[i]] = mywords[i]
print(d)
