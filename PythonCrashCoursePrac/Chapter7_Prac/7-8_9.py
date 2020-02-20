sandwich_orders = ['tuna', 'pastrami', 'beef', 'chicken', 'pastrami', 'pastrami']
finished_sandwiches = []
print('We are out of pastrami!')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove("pastrami")
while sandwich_orders:
    for sandwich in sandwich_orders:
        sandwich_made = sandwich_orders.pop()
        print('I made your {} sandwich.'.format(sandwich_made))
        finished_sandwiches.append(sandwich_made)
print('Sandwich all done, they are:')
for sandwich in finished_sandwiches:
    print('{} sandwich'.format(sandwich.title()))
