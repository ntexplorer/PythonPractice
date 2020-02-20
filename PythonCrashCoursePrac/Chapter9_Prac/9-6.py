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


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def add_flavor(self, flavor):
        self.flavors.append(flavor)

    def display_flavor(self):
        print("We now have the flavor below:")
        for i in self.flavors:
            print(i)


DQ = IceCreamStand("Diary Queen", "IceCreamStand")
DQ.describe_restaurant()
DQ.add_flavor("Chocolate")
DQ.add_flavor("Vanilla")
DQ.add_flavor("Mocha")
DQ.display_flavor()
