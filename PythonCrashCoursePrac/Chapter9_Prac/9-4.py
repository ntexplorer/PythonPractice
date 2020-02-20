class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.name.title())
        print(self.type.lower())
        print('The number of people served here is {}'.format(str(self.number_served)))

    def open_restaurant(self):
        print("The restaurant is open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        if number >= 0:
            self.number_served += number
        else:
            print("The number severed can't be negative!")


restaurant = Restaurant("Nandos", "Fast Food")
restaurant.describe_restaurant()
restaurant.open_restaurant()

# restaurant.number_served = 23
# restaurant.describe_restaurant()

restaurant.set_number_served(23)
restaurant.increment_number_served(46)
restaurant.describe_restaurant()
