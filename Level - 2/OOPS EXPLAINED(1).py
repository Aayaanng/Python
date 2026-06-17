"""
===========================================
OBJECT ORIENTED PROGRAMMING (OOP) IN PYTHON
===========================================
A complete guide with all 5 major concepts:
1. Class & Object
2. Encapsulation
3. Inheritance
4. Polymorphism
5. Abstraction
"""

# ===========================================
# 1️⃣ CLASS & OBJECT (Base of OOPS)
# ===========================================

# 🧠 REAL-LIFE EXAMPLE:
# Class = Blueprint
# Object = Real thing made from a blueprint
# 👉 Car is a class
# 👉 My car, your car are objects

# 🧪 CODE EXAMPLE:
class Car:                     # Class: blueprint/design of a car
    def start(self):           # Method: behavior of the car
        print("Car is starting")

# Object creation
my_car = Car()                 # Object: actual car created from the class
my_car.start()                 # Calling the method on the object

# 📌 EXPLANATION:
print("\n" + "="*50)
print("📌 Class & Object: Class is a design, object is the actual thing we use.")
print("   Just like a house blueprint (class) vs the actual house built (object)")
print("="*50 + "\n")


# ===========================================
# 2️⃣ ENCAPSULATION (Data Protection)
# ===========================================

# 🧠 REAL-LIFE EXAMPLE:
# ATM Machine
# You can withdraw money
# You cannot see how ATM works inside

# 🧪 CODE EXAMPLE:
class ATM:
    def __init__(self):
        self.__balance = 5000   # Private data (hidden from outside)
                                # __ (double underscore) makes it private

    def withdraw(self, amount): # Public method to access private data
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"✅ Withdraw successful! Remaining balance: ₹{self.__balance}")
        else:
            print(f"❌ Insufficient balance! Available: ₹{self.__balance}")

# Creating ATM object
atm = ATM()
print("🏧 ATM Machine Demo:")
atm.withdraw(2000)              # Trying to withdraw 2000
atm.withdraw(4000)              # Trying to withdraw 4000 (should fail)
# print(atm.__balance)          # ❌ ERROR: Cannot access private variable directly!

# 📌 EXPLANATION:
print("\n" + "="*50)
print("📌 Encapsulation: Data is hidden, user can access only through methods.")
print("   The balance is protected - you can't change it directly, only through withdraw()")
print("="*50 + "\n")


# ===========================================
# 3️⃣ INHERITANCE (Reuse of Code)
# ===========================================

# 🧠 REAL-LIFE EXAMPLE:
# Parent → Child
# Child gets properties from parent
# 👉 Vehicle → Car

# 🧪 CODE EXAMPLE:
class Vehicle:                  # Parent class (base class)
    def fuel(self):
        print("⛽ Uses fuel")
    
    def move(self):
        print("🚗 Vehicle can move")

class Car(Vehicle):             # Child class (derived class)
                                # Inherits all features from Vehicle
    def wheels(self):
        print("🚙 Car has 4 wheels")
    
    def honk(self):             # Child's own method
        print("🔊 Beep beep!")

print("🚘 Inheritance Demo:")
c = Car()                       # Creating child class object
c.fuel()                        # Inherited method from Vehicle (parent)
c.move()                        # Inherited method from Vehicle (parent)
c.wheels()                      # Child's own method
c.honk()                        # Child's own method

# 📌 EXPLANATION:
print("\n" + "="*50)
print("📌 Inheritance: Child class can use parent class features.")
print("   Car gets fuel() and move() from Vehicle, so we don't need to rewrite them")
print("="*50 + "\n")


# ===========================================
# 4️⃣ POLYMORPHISM (Many Forms)
# ===========================================

# 🧠 REAL-LIFE EXAMPLE:
# Same action, different behavior
# 👉 Teacher teaches
# 👉 Online teacher teaches
# 👉 Sports teacher teaches differently

# 🧪 CODE EXAMPLE:
class Teacher:                  # Parent class
    def teach(self):            # Method with specific behavior
        print("📚 Teaching in classroom")

class OnlineTeacher(Teacher):   # Child class
    def teach(self):            # Same method name, but DIFFERENT behavior
        print("💻 Teaching online via Zoom")

class SportsTeacher(Teacher):   # Another child class
    def teach(self):            # Same method name, different behavior again
        print("🏃 Teaching sports on the field")

print("🎭 Polymorphism Demo:")
t1 = Teacher()                  # Object of parent class
t2 = OnlineTeacher()            # Object of child class
t3 = SportsTeacher()            # Object of another child class

t1.teach()                      # Output: Teaching in classroom
t2.teach()                      # Output: Teaching online via Zoom
t3.teach()                      # Output: Teaching sports on the field

# 📌 EXPLANATION:
print("\n" + "="*50)
print("📌 Polymorphism: Same function name (teach), different output.")
print("   This is polymorphism - 'many forms' of the same method")
print("="*50 + "\n")


# ===========================================
# 5️⃣ ABSTRACTION (Show Only Important Things)
# ===========================================

# 🧠 REAL-LIFE EXAMPLE:
# Mobile Phone
# You press call button
# You don't know internal working

# 🧪 CODE EXAMPLE:
from abc import ABC, abstractmethod   # Import ABC (Abstract Base Class)

class Shape(ABC):                     # Abstract class (incomplete blueprint)
    @abstractmethod                   # Decorator that makes this method mandatory
    def area(self):                   # Abstract method (no implementation)
        pass                          # Child classes MUST implement this
    
    @abstractmethod
    def perimeter(self):              # Another abstract method
        pass

class Square(Shape):                  # Concrete class (complete implementation)
    def __init__(self, side):
        self.side = side
    
    def area(self):                   # Must implement area() because Shape said so
        result = self.side * self.side
        print(f"📐 Square area = {result} (side × side)")
        return result
    
    def perimeter(self):              # Must implement perimeter()
        result = 4 * self.side
        print(f"📏 Square perimeter = {result} (4 × side)")
        return result

class Circle(Shape):                  # Another concrete class
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):                   # Different implementation for circle
        result = 3.14 * self.radius * self.radius
        print(f"⚪ Circle area = {result} (π × r²)")
        return result
    
    def perimeter(self):              # Different implementation for circle
        result = 2 * 3.14 * self.radius
        print(f"📏 Circle circumference = {result} (2πr)")
        return result

print("🔍 Abstraction Demo:")
square = Square(5)                    # Creating square with side 5
circle = Circle(3)                    # Creating circle with radius 3

square.area()                         # Shows only area calculation
square.perimeter()                    # Shows only perimeter calculation
circle.area()                         # Different formula, same method name
circle.perimeter()                    # Different formula, same method name

# 📌 EXPLANATION:
print("\n" + "="*50)
print("📌 Abstraction: Only important methods shown, internal details hidden.")
print("   Shape shows 'you must have area() and perimeter()' but hides HOW to calculate them")
print("="*50 + "\n")


# ===========================================
# 🧠 SIMPLE TRICK TO REMEMBER OOPS
# ===========================================

print("\n" + "🧠" + "="*48)
print(" SIMPLE TRICK TO REMEMBER OOPS CONCEPTS")
print("="*50)

print("\n┌─────────────────┬────────────────────────────────────┐")
print("│   Concept       │   Meaning                          │")
print("├─────────────────┼────────────────────────────────────┤")
print("│ Class           │ Blueprint                          │")
print("│ Object          │ Real thing                         │")
print("│ Encapsulation   │ Data hiding                        │")
print("│ Inheritance     │ Parent → Child                     │")
print("│ Polymorphism    │ Same action, different result      │")
print("│ Abstraction     │ Hide internal details              │")
print("└─────────────────┴────────────────────────────────────┘")

print("\n" + "🎯" + "="*48)
print(" QUICK MEMORY TRICK: CEO PIA")
print("="*48)
print("C - Class & Object")
print("E - Encapsulation")
print("O - (I) Inheritance")
print("P - Polymorphism")
print("I - (A) Abstraction")
print("A - All together!")
print("="*50)


# ===========================================
# BONUS: Demonstration of all concepts working together
# ===========================================

print("\n" + "🌟" + "="*48)
print(" BONUS: All OOP Concepts Working Together!")
print("="*48)

class BankAccount(ABC):                     # Abstraction + Inheritance
    """Abstract base class for bank accounts"""
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.__balance = 0                  # Encapsulation (private)
    
    def deposit(self, amount):              # Public method
        if amount > 0:
            self.__balance += amount
            print(f"💰 Deposited ₹{amount}. New balance: ₹{self.__balance}")
        else:
            print("❌ Invalid deposit amount")
    
    def get_balance(self):                  # Encapsulation (getter)
        return self.__balance
    
    @abstractmethod
    def account_type(self):                 # Abstraction
        pass

class SavingsAccount(BankAccount):          # Inheritance
    def account_type(self):                 # Polymorphism
        return "Savings Account (4% interest)"

class CurrentAccount(BankAccount):          # Inheritance
    def account_type(self):                 # Polymorphism
        return "Current Account (No interest)"

# Creating objects
print("\n🏦 Banking System Demo:")
savings = SavingsAccount("Alice")
current = CurrentAccount("Bob")

savings.deposit(5000)
current.deposit(10000)

print(f"\n{savings.account_holder}'s {savings.account_type()}")
print(f"Balance: ₹{savings.get_balance()}")

print(f"\n{current.account_holder}'s {current.account_type()}")
print(f"Balance: ₹{current.get_balance()}")

print("\n" + "="*50)
print("✅ All OOP concepts demonstrated successfully!")
print("="*50)