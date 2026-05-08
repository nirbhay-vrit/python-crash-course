# ---------------------------------------------------------
# DAY 9 | PUTTING IT ALL TOGETHER
# All 4 OOP Pillars in two complete mini-projects:
#   1. Animal Kingdom — Encapsulation + Inheritance + Polymorphism
#   2. Online Store   — all 4 pillars including Abstraction
# ---------------------------------------------------------

from abc import ABC, abstractmethod


# ═════════════════════════════════════════════════════════
# MINI PROJECT 1: Animal Kingdom
# Demonstrates: Encapsulation, Inheritance, Polymorphism,
#               Special methods
# ═════════════════════════════════════════════════════════

class Animal:
    """Base class for all animals — Encapsulation + shared behaviour."""

    def __init__(self, name, age):
        self.name = name
        self.age  = age
        self.__health = 100             # private — encapsulation

    def eat(self):
        self.__health = min(100, self.__health + 10)
        print(f"  {self.name} eats. Health: {self.__health}")

    def get_health(self):
        return self.__health

    def speak(self):                    # meant to be overridden — polymorphism
        return f"{self.name} makes a sound."

    def __str__(self):
        return f"{self.__class__.__name__}({self.name}, {self.age} yrs)"

    def __eq__(self, other):
        return self.name == other.name and type(self) is type(other)


class Dog(Animal):
    """Dog inherits Animal, overrides speak(), adds fetch()."""

    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):                    # polymorphism — overrides Animal.speak()
        return f"{self.name} says: Woof!"

    def fetch(self, item):
        print(f"  {self.name} fetches the {item}!")

    def __str__(self):
        return f"Dog({self.name}, {self.age} yrs, {self.breed})"


class Cat(Animal):
    """Cat inherits Animal, overrides speak(), adds purr()."""

    def __init__(self, name, age, indoor):
        super().__init__(name, age)
        self.indoor = indoor

    def speak(self):
        return f"{self.name} says: Meow!"

    def purr(self):
        print(f"  {self.name} purrs contentedly...")

    def __str__(self):
        loc = "indoor" if self.indoor else "outdoor"
        return f"Cat({self.name}, {self.age} yrs, {loc})"


class Parrot(Animal):
    def __init__(self, name, age, phrase):
        super().__init__(name, age)
        self.phrase = phrase

    def speak(self):
        return f"{self.name} says: {self.phrase}"


class Zoo:
    """Collection of animals — uses __len__, __contains__, __str__."""

    def __init__(self, name):
        self.name    = name
        self._animals = []              # protected convention

    def add(self, animal):
        self._animals.append(animal)
        print(f"  + {animal.name} joined {self.name} Zoo.")

    def __len__(self):
        return len(self._animals)

    def __contains__(self, animal):
        return animal in self._animals

    def __str__(self):
        return f"{self.name} Zoo — {len(self)} animals"

    def morning_roll_call(self):
        print(f"\n  [{self.name} Zoo — Morning Roll Call]")
        for a in self._animals:
            print(f"    {a.speak()}")

    def feeding_time(self):
        print(f"\n  [{self.name} Zoo — Feeding Time]")
        for a in self._animals:
            a.eat()


print("=" * 54)
print("  MINI PROJECT 1: Animal Kingdom")
print("=" * 54)

zoo = Zoo("Happy Paws")
zoo.add(Dog("Rex",    3, "Labrador"))
zoo.add(Cat("Luna",   2, True))
zoo.add(Parrot("Polly", 5, "Crackers!"))
zoo.add(Dog("Buddy",  4, "Poodle"))

print(zoo)                          # Happy Paws Zoo — 4 animals
zoo.morning_roll_call()
zoo.feeding_time()

# isinstance check — polymorphism awareness:
print("\n  [Type checks]")
for animal in zoo._animals:
    tag = "Dog" if isinstance(animal, Dog) else ("Cat" if isinstance(animal, Cat) else "Other")
    print(f"    {animal.name}: {tag}")


# ═════════════════════════════════════════════════════════
# MINI PROJECT 2: Online Store
# Demonstrates: all 4 pillars — Encapsulation, Inheritance,
#               Polymorphism, Abstraction, Special methods
# ═════════════════════════════════════════════════════════

# ── ABSTRACTION: define the payment contract ──────────────
class PaymentMethod(ABC):
    @abstractmethod
    def charge(self, amount: float) -> bool:
        pass

    @abstractmethod
    def name(self) -> str:
        pass


# ── INHERITANCE + ENCAPSULATION: concrete payment methods ─
class CreditCard(PaymentMethod):
    def __init__(self, holder, last4):
        self.__holder = holder          # private — encapsulation
        self.__last4  = last4

    def name(self):
        return f"Credit Card (...{self.__last4})"

    def charge(self, amount):
        print(f"    Charged ${amount:.2f} to card ending {self.__last4} — approved.")
        return True


class Wallet(PaymentMethod):
    def __init__(self, owner, balance):
        self.__owner   = owner
        self.__balance = balance

    def name(self):
        return f"{self.__owner}'s Wallet"

    def charge(self, amount):
        if amount > self.__balance:
            print(f"    Wallet insufficient. Need ${amount:.2f}, have ${self.__balance:.2f}.")
            return False
        self.__balance -= amount
        print(f"    Charged ${amount:.2f} from wallet. Remaining: ${self.__balance:.2f}.")
        return True


# ── ENCAPSULATION: Product ────────────────────────────────
class Product:
    def __init__(self, name, price, stock):
        self.name   = name
        self.__price = price            # private
        self.__stock = stock            # private

    @property
    def price(self):
        return self.__price

    @property
    def stock(self):
        return self.__stock

    def is_available(self, qty=1):
        return self.__stock >= qty

    def reduce_stock(self, qty):
        if self.is_available(qty):
            self.__stock -= qty
            return True
        return False

    def __str__(self):
        return f"{self.name} (${self.__price:.2f}, {self.__stock} in stock)"

    def __eq__(self, other):
        return self.name == other.name


# ── INHERITANCE + POLYMORPHISM: product types ─────────────
class DigitalProduct(Product):
    """Digital products never go out of stock."""

    def is_available(self, qty=1):      # overrides — always available
        return True

    def reduce_stock(self, qty):        # overrides — nothing to reduce
        return True

    def __str__(self):
        return f"[Digital] {self.name} (${self.price:.2f}, unlimited)"


class PhysicalProduct(Product):
    def __init__(self, name, price, stock, weight_kg):
        super().__init__(name, price, stock)
        self.weight_kg = weight_kg

    def __str__(self):
        return f"[Physical] {self.name} (${self.price:.2f}, {self.stock} in stock, {self.weight_kg}kg)"


# ── Shopping Cart ─────────────────────────────────────────
class ShoppingCart:
    def __init__(self, customer_name):
        self.customer = customer_name
        self.__items  = []              # private list of (product, qty)

    def add(self, product, qty=1):
        if not product.is_available(qty):
            print(f"    Sorry, {product.name} is out of stock.")
            return
        self.__items.append((product, qty))
        print(f"    Added {qty}x {product.name} to cart.")

    def total(self):
        return sum(p.price * q for p, q in self.__items)

    def checkout(self, payment: PaymentMethod):
        if not self.__items:
            print("    Cart is empty!")
            return
        print(f"\n    === Checkout for {self.customer} ===")
        for product, qty in self.__items:
            print(f"      {qty}x {product.name}  ${product.price * qty:.2f}")
        print(f"    Total: ${self.total():.2f}")
        print(f"    Paying via {payment.name()}...")

        if payment.charge(self.total()):
            for product, qty in self.__items:
                product.reduce_stock(qty)
            print("    Order confirmed! Thank you.")
            self.__items.clear()
        else:
            print("    Payment failed. Order not placed.")

    def __len__(self):
        return sum(q for _, q in self.__items)

    def __str__(self):
        return f"{self.customer}'s cart ({len(self)} item(s), total ${self.total():.2f})"


print("\n" + "=" * 54)
print("  MINI PROJECT 2: Online Store")
print("=" * 54)

# Set up products
py_course = DigitalProduct("Python Course",     49.99, 0)   # unlimited stock
headphones = PhysicalProduct("Headphones",      79.99, 5, 0.3)
notebook   = PhysicalProduct("Notebook",        12.99, 2, 0.5)

print("\n  [Products in store]")
for p in [py_course, headphones, notebook]:
    print(f"    {p}")

# Alice shops with a credit card
print("\n  [Alice's order]")
alice_cart = ShoppingCart("Alice")
alice_cart.add(py_course)
alice_cart.add(headphones)
print(alice_cart)

alice_payment = CreditCard("Alice Smith", "4321")
alice_cart.checkout(alice_payment)

# Bob tries with a wallet (not enough funds)
print("\n  [Bob's order]")
bob_cart = ShoppingCart("Bob")
bob_cart.add(notebook, 2)
print(bob_cart)

bob_payment = Wallet("Bob", 10.00)   # only $10 — not enough for $25.98
bob_cart.checkout(bob_payment)

# Remaining stock
print("\n  [Updated stock]")
for p in [py_course, headphones, notebook]:
    print(f"    {p}")
