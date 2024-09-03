class Animal:
    name = ""

    def set_name(self, name):
        self.name = name

    def make_sound(self):
        return "Generic animal sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Using the Animal class
generic_animal = Animal()
generic_animal.set_name("Generic Animal")
print(generic_animal.name)
print(generic_animal.make_sound())

# Using the Dog class (inherits from Animal)
dog = Dog()
dog.set_name("Buddy")
print(dog.name)
print(dog.make_sound())

# Using the Cat class (inherits from Animal)
cat = Cat()
cat.set_name("Whiskers")
print(cat.name)
print(cat.make_sound())
