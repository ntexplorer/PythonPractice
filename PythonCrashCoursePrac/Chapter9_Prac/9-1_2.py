class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(self.name.title())
        print(self.type.lower())

    def open_restaurant(self):
        print("The restaurant is open!")


restaurant = Restaurant("Nandos", "Fast Food")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant2 = Restaurant("KFC", "Chicken")
restaurant2.describe_restaurant()
restaurant2.open_restaurant()
