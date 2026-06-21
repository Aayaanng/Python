class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"

    # Constructor method (runs when object is created)
    def __init__(self, name, age):
        self.name = name   # Instance attribute
        self.age = age     # Instance attribute

    # Instance method
    def bark(self):
        return f"{self.name} says: Woof!"

    def __str__(self):
        return f"Dog(name={self.name}, age={self.age})"

dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.name)     # Buddy
print(dog2.age)      # 5
print(dog1.bark())   # Buddy says: Woof!
print(dog1)          # Dog(name=Buddy, age=3)

dog1.name = "Charlie"      # Modify attribute
print(dog1.name)           # Charlie

print(dog1.species)        # Canis familiaris (class attribute)
print(Dog.species)         # Same — accessed via class name too

dog1 = Dog("Mischief", 8)
print(dog1.name,"is", dog1.age)
