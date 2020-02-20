t1 = True
t2 = False
a, b, c = 100, 200, 300
print(a < b < c, t1 and t2, (not t1) or (not t2))

for i in range(40, 0, -5):
    if (i % 3 == 0):
        print(i, end=',')

st1 = 'He had a run in the park.'
st2 = 'The family went to the park to feed the ducks.'
st3 = ''
for c in st1:
    if c in st2:
        st3 += c
print('\n' + st3)

for i in range(3, 40):
    if i == 36:
        break
    if (i % 2 == 0) or (i % 3 == 0) or (i % 5 == 0):
        continue
    print(i, end=' ')

st = 'Hello World!'
st2 = st[::-1]
print('\n' + st2 + '\n')


def foo(a, b):
    return a + b, a // b, a % b


i, j, k = foo(20, 5)
print("{}, {}, {}".format(i, j, k))
