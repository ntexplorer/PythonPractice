sandwich_orders = ['tuna', 'pastrami', 'beef', 'chicken', 'pastrami', 'pastrami']
finished_sandwiches = []
print('We are out of pastrami!')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove("pastrami")

print(sandwich_orders)
for sandwich in sandwich_orders:
    print("############")
    print('I made your {} sandwich.'.format(sandwich))
    sandwich_made = sandwich_orders.pop()
    finished_sandwiches.append(sandwich_made)
    print(sandwich)
    print(sandwich_made)
    print(sandwich_orders)
    print(finished_sandwiches)
    print("############\n")
print('Sandwich all done, they are:')
for sandwich in finished_sandwiches:
    print('{} sandwich'.format(sandwich.title()))
