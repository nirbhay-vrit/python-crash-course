# ---------------------------------------------------------
# DAY 8 | TOPIC 4: METHODS — Giving Objects Behaviour
# Methods are functions defined INSIDE a class.
# They define what an object CAN DO.
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: WHAT IS A METHOD?
# ─────────────────────────────────────────────────────────
# A method is just a function defined inside a class.
# The difference from a regular function:
#   - It takes `self` as its first parameter (always!)
#   - You call it using dot notation:  object.method()
#
#   ATTRIBUTES  = what the object KNOWS   (data)
#   METHODS     = what the object CAN DO  (behaviour)

class Dog:
    def __init__(self, name, breed):
        self.name  = name
        self.breed = breed

    def bark(self):                  # ← method: no extra parameters
        print(f"{self.name} says: Woof!")

    def introduce(self):             # ← method: uses self.name and self.breed
        print(f"I am {self.name}, a {self.breed}.")

rex   = Dog("Rex",   "Labrador")
buddy = Dog("Buddy", "Poodle")

print("--- Calling methods ---")
rex.bark()        # Rex says: Woof!
buddy.bark()      # Buddy says: Woof!
rex.introduce()   # I am Rex, a Labrador.

# When rex.bark() runs:   self = rex,   so self.name = "Rex"
# When buddy.bark() runs: self = buddy, so self.name = "Buddy"
# The SAME method produces different output for different objects!


# ─────────────────────────────────────────────────────────
# SECTION 2: METHODS WITH EXTRA PARAMETERS
# ─────────────────────────────────────────────────────────
# Methods can take extra parameters AFTER self.
# self is always first — you don't pass it yourself.

class Calculator:
    def __init__(self, brand):
        self.brand = brand

    def add(self, a, b):          # self + two extra params
        return a + b

    def multiply(self, a, b):
        return a * b

    def describe(self):           # no extra params, just self
        print(f"This is a {self.brand} calculator.")

calc = Calculator("Casio")
print("\n--- Methods with parameters ---")
calc.describe()
print(calc.add(3, 4))          # 7
print(calc.multiply(5, 6))     # 30
print(calc.add(100, 200))      # 300


# ─────────────────────────────────────────────────────────
# SECTION 3: METHODS THAT MODIFY ATTRIBUTES
# ─────────────────────────────────────────────────────────
# Methods can READ and CHANGE the object's own attributes (via self).
# This is how objects manage their own state.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner   = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"  {self.owner} deposited {amount}. Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"  Not enough money! Balance: {self.balance}")
        else:
            self.balance -= amount
            print(f"  {self.owner} withdrew {amount}. Balance: {self.balance}")

    def show_balance(self):
        print(f"  {self.owner}'s balance: {self.balance}")

print("\n--- Bank account methods ---")
account = BankAccount("Alice", 100)
account.show_balance()      # 100
account.deposit(50)         # deposits 50  → 150
account.withdraw(30)        # withdraws 30 → 120
account.withdraw(200)       # not enough!
account.show_balance()      # 120


# ─────────────────────────────────────────────────────────
# SECTION 4: METHODS THAT RETURN VALUES
# ─────────────────────────────────────────────────────────
# Methods can return values just like regular functions.
# Use return when you want to USE the result somewhere else.

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):             # returns a value
        return (self.celsius * 9 / 5) + 32

    def to_kelvin(self):
        return self.celsius + 273.15

    def describe(self):
        if self.celsius < 0:
            return "freezing"
        elif self.celsius < 15:
            return "cold"
        elif self.celsius < 25:
            return "comfortable"
        else:
            return "hot"

print("\n--- Methods returning values ---")
temp = Temperature(25)
f = temp.to_fahrenheit()     # save the returned value
k = temp.to_kelvin()
print(f"{temp.celsius}°C  =  {f}°F")
print(f"{temp.celsius}°C  =  {k} K")
print(f"It is {temp.describe()} outside.")

# Different temperatures:
for c in [0, 15, 37, 100]:
    t = Temperature(c)
    print(f"  {c}°C → {t.to_fahrenheit():.1f}°F ({t.describe()})")


# ─────────────────────────────────────────────────────────
# SECTION 5: METHODS CALLING OTHER METHODS
# ─────────────────────────────────────────────────────────
# A method can call another method on the same object using self.

class Student:
    def __init__(self, name, scores):
        self.name   = name
        self.scores = scores

    def get_average(self):           # helper method
        return sum(self.scores) / len(self.scores)

    def get_grade(self):             # calls get_average()
        avg = self.get_average()     # ← calling another method via self
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        else:
            return "F"

    def report(self):                # calls both helpers
        avg   = self.get_average()
        grade = self.get_grade()
        print(f"  {self.name}: avg={avg:.1f}, grade={grade}")

print("\n--- Methods calling other methods ---")
alice = Student("Alice",   [88, 92, 79])
bob   = Student("Bob",     [65, 70, 58])
diana = Student("Diana",   [95, 91, 97])

alice.report()    # Alice: avg=86.3, grade=B
bob.report()      # Bob:   avg=64.3, grade=C
diana.report()    # Diana: avg=94.3, grade=A


# ─────────────────────────────────────────────────────────
# SECTION 6: MANY OBJECTS — INDEPENDENT STATE
# ─────────────────────────────────────────────────────────
# Each object keeps its OWN state.
# Calling a method on one object does NOT affect others.

print("\n--- Independent state ---")
acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob",   500)

acc1.deposit(200)     # only Alice's account changes
acc2.withdraw(100)    # only Bob's account changes

acc1.show_balance()   # Alice: 1200
acc2.show_balance()   # Bob:   400
