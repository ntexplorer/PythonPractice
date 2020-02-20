brand = {'Carhartt': 'Jacket',
         'RedWing': 'Workboot',
         'Levis': 'Jeans'}
for logo, product in brand.items():
    print('{} is the best product of {}.'.format(product, logo))
for logo in brand.keys():
    print("{} is a good brand.".format(logo))
for product in brand.values():
    print("{} is one kind of product.".format(product))
