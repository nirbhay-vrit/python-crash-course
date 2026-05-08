# ---------------------------------------------------------
# DAY 9 | TOPIC 3: ABSTRACTION — Hide Complexity, Show Simplicity
# Abstraction means: give the user a simple interface,
# hide how it actually works underneath.
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: WHAT IS ABSTRACTION?
# ─────────────────────────────────────────────────────────
# Real-world analogy:
#   You drive a car — you press the gas pedal and it moves.
#   You do NOT need to understand combustion, fuel injection,
#   gear ratios, or the ECU to drive.
#   The car HIDES complexity behind a simple interface.
#
# In OOP, abstraction means:
#   - Define WHAT an object must be able to do (the interface)
#   - Hide HOW it does it (the implementation)
#
# Python uses ABSTRACT BASE CLASSES (ABC) for this.
# An abstract class defines methods that MUST be implemented
# by every subclass — but the abstract class itself cannot
# be instantiated (you can't create objects from it directly).

from abc import ABC, abstractmethod


# ─────────────────────────────────────────────────────────
# SECTION 2: ABSTRACT BASE CLASS BASICS
# ─────────────────────────────────────────────────────────
# Inherit from ABC and mark methods with @abstractmethod.
# Any subclass MUST implement all abstract methods,
# or Python will raise a TypeError.

class Shape(ABC):                   # ← inherits ABC to become abstract
    def __init__(self, colour):
        self.colour = colour

    @abstractmethod                 # ← subclasses MUST implement this
    def area(self):
        pass                        # no body needed — it's a contract

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):             # NOT abstract — shared behaviour
        print(f"{self.colour} {self.__class__.__name__}: "
              f"area={self.area():.2f}, perimeter={self.perimeter():.2f}")


# Can you create a Shape directly? NO:
# s = Shape("red")  → TypeError: Can't instantiate abstract class Shape


class Circle(Shape):
    def __init__(self, colour, radius):
        super().__init__(colour)
        self.radius = radius

    def area(self):                 # MUST implement this
        return 3.14159 * self.radius ** 2

    def perimeter(self):            # MUST implement this
        return 2 * 3.14159 * self.radius


class Rectangle(Shape):
    def __init__(self, colour, w, h):
        super().__init__(colour)
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)


print("--- Abstract base class ---")
shapes = [Circle("red", 5), Rectangle("blue", 4, 6)]
for s in shapes:
    s.describe()

# red Circle:    area=78.54, perimeter=31.42
# blue Rectangle: area=24.00, perimeter=20.00


# ─────────────────────────────────────────────────────────
# SECTION 3: WHAT HAPPENS WHEN YOU SKIP AN ABSTRACT METHOD
# ─────────────────────────────────────────────────────────

class IncompleteShape(Shape):
    def area(self):
        return 0
    # forgot to implement perimeter() !

# Trying to create an object of IncompleteShape would give:
# TypeError: Can't instantiate abstract class IncompleteShape
# with abstract method perimeter
#
# This is abstraction ENFORCING the contract.
# Uncomment to see:
# bad = IncompleteShape("green")

print("\n--- Contract enforcement ---")
print("IncompleteShape is missing perimeter() — cannot instantiate it.")


# ─────────────────────────────────────────────────────────
# SECTION 4: PRACTICAL ABSTRACTION — PAYMENT SYSTEM
# ─────────────────────────────────────────────────────────
# A real-world example: different payment methods all support pay().
# The caller doesn't need to know HOW each payment works.

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass


class CreditCard(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        print(f"  Charging ${amount:.2f} to card ending in {self.card_number[-4:]}.")

    def refund(self, amount):
        print(f"  Refunding ${amount:.2f} to card ending in {self.card_number[-4:]}.")


class PayPal(PaymentMethod):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"  Sending ${amount:.2f} via PayPal ({self.email}).")

    def refund(self, amount):
        print(f"  PayPal refund of ${amount:.2f} to {self.email}.")


class CashPayment(PaymentMethod):
    def pay(self, amount):
        print(f"  Received ${amount:.2f} cash.")

    def refund(self, amount):
        print(f"  Returning ${amount:.2f} cash.")


def process_order(payment: PaymentMethod, amount: float):
    print(f"Processing order of ${amount:.2f}:")
    payment.pay(amount)             # caller doesn't care HOW it pays


print("\n--- Payment abstraction ---")
methods = [
    CreditCard("4111111111111234"),
    PayPal("alice@example.com"),
    CashPayment(),
]

for method in methods:
    process_order(method, 99.99)

# Each payment method hides its own complexity.
# process_order() just calls .pay() and trusts the contract.


# ─────────────────────────────────────────────────────────
# SECTION 5: ABSTRACTION vs ENCAPSULATION — SIDE BY SIDE
# ─────────────────────────────────────────────────────────
# These two are often confused. They are different pillars:
#
# ENCAPSULATION (Day 8):
#   Bundle data + methods together in a class.
#   Control ACCESS to internal details (private attributes).
#   HOW you package and protect data.
#
# ABSTRACTION (today):
#   Define WHAT an object must do (the contract/interface).
#   Hide HOW it does it from the user.
#   The user only sees the simple "what", not the complex "how".
#
# Analogy:
#   Encapsulation = the engine bay of a car is sealed.
#   Abstraction   = the dashboard shows you speed/fuel, not engine internals.

class DatabaseConnection(ABC):     # ABSTRACTION: defines the contract
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def query(self, sql):
        pass

    @abstractmethod
    def disconnect(self):
        pass


class MySQLConnection(DatabaseConnection):  # ENCAPSULATION: hides MySQL details
    def __init__(self, host, port):
        self.__host = host          # private — encapsulation
        self.__port = port

    def connect(self):
        print(f"  MySQL connected to {self.__host}:{self.__port}")

    def query(self, sql):
        print(f"  MySQL running: {sql}")

    def disconnect(self):
        print("  MySQL disconnected.")


class SQLiteConnection(DatabaseConnection):
    def __init__(self, filepath):
        self.__filepath = filepath

    def connect(self):
        print(f"  SQLite opened {self.__filepath}")

    def query(self, sql):
        print(f"  SQLite running: {sql}")

    def disconnect(self):
        print("  SQLite closed.")


def run_report(db: DatabaseConnection):
    db.connect()
    db.query("SELECT * FROM users WHERE active = 1")
    db.disconnect()


print("\n--- Abstraction vs Encapsulation ---")
print("MySQL:")
run_report(MySQLConnection("localhost", 3306))
print("SQLite:")
run_report(SQLiteConnection("data.db"))

# run_report doesn't know (or care) which database it's talking to.
# That is abstraction at work.
