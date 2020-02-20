total = i = 0
while True:
    i += 1
    total += i
    if total > 10000:
        break
print('The sum of intergers from 1 to {} is {}.'.format(i, total))

total = i = 0
while total < 10000:
    i += 1
    total += i
print('The sum of intergers from 1 to {} is {}.'.format(i, total))
