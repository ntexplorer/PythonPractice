name = input("Enter your name: ")

class Person:
    def __init__(self, name):
        self.name = name.capitalize()

    def say_hi(self):
        print("Hello {}, this is my first OOP program.".format(self.name))

p = Person(name)
p.say_hi()
