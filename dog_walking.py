class Pets:

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

    def walk(self):
        for dog in self.dogs:
            print(dog.walk())

class Dog:

    species = "mammal"
    is_hungry = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return '{} is {} years old'.format(self.name, self.age)

    def eat(self):
        self.is_hungry = False

    def walk(self):
        return "{} is walking!".format(self.name)

dog_list = [Dog("Tom", 6), Dog("Fletcher", 7), Dog("Larry", 9)]

pets = Pets(dog_list)

pets.walk()