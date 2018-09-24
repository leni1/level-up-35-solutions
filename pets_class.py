class Pets:

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

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

    def speak(self, sound):
        return "%s says %s" % (self.name, sound)

dog_list = [Dog("Tom", 6), Dog("Fletcher", 7), Dog("Larry", 9)]

pets = Pets(dog_list)

print("I have {} dogs.".format(len(pets.dogs)))

for dog in pets.dogs:
    print("{} is {}.".format(dog.name, dog.age))
print("And they're all {}s of course.".format(dog.species))

are_hungry = False
for dog in pets.dogs:
    if dog.is_hungry:
        are_hungry = True

if are_hungry:
    print("My dogs are hungry.")
else:
    print("My dogs are not hungry.")
