class Employee:
    def __init__(self, name, project, salary):
        self.name = name
        self._project = project
        self.__salary = salary  
# inheritence
print("Inheritance")
class parent:
    def speak(self):
        print("i can speak")
class child(parent):
    def dance(self):
        print("i can dance")
c = child()
c.speak()
c.dance()
# encapsulation
print("Encapsulation")
class bank_account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance  # private 
    def deposit(self, amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance
account = bank_account("123456789", 10000)
account.deposit(5000)
print(account.get_balance())  
#Polymorphism
class dog:
    def bark(self):
        print("Woof!")
class cat:
    def bark(self):
        print("Meow!")
animals = [dog(), cat()]
for animal in animals:
    animal.bark() 