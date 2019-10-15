class User():
    def __init__(self, first, last, gender, age):
        self.first_name = first
        self.last_name = last
        self.gender = gender
        self.age = age
        self.full_name = self.first_name + " " + self.last_name

    def describe_user(self):
        print("The name of the user is " + self.full_name + ".")
        print("The user's gender is " + self.gender + ".")
        print("The user is " + str(self.age) + " years old.")

    def greet_user(self):
        if self.gender.lower() == "male":
            print("Greetings, Mr. " + self.last_name.title() + "!")
        elif self.gender.lower() == "female":
            print("Greetings, Miss " + self.last_name.title() + "!")

user1 = User("zhichao", "li", "male", 27)
user2 = User("juan", "zhang", "female", 28)
user3 = User("Tian", "ZHANG", "male", 26)

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()
