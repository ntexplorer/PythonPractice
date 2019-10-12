brand = {"carhartt": {
    "product": "jacket",
    'price': "70",
    'color': 'yellow'
},
    'redwing': {
    "product": "Workboot",
    "price": "300",
    'color': "brown"
},
    "barbour": {
    "product": "raincoat",
    "price": "200",
    "color": "olive"
}}
for brand_name, brand_info in brand.items():
    print("The famous product for {} is: ".format(brand_name.title()))
    product = brand_info["product"]
    price = brand_info["price"]
    color = brand_info['color']
    print("\t{}, which costs {} pounds and usually comes in {}.".format(product.title(), price, color))
