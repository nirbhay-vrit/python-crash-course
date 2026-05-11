# ---------------------------------------------------------
# SOLUTION 4: METHODS
# ---------------------------------------------------------
# A method is just a function defined INSIDE a class.
# Its first parameter is always `self` (the object it's called on).


# EXERCISE 1: Add methods to Person.
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def greet(self):
        print(f"Hello, my name is {self.full_name()}!")  # method calling method!

alice = Person("Alice", "Wong", 28)
bob = Person("Bob", "Smith", 35)

print(alice.full_name())
alice.greet()
print(bob.full_name())
bob.greet()


# EXERCISE 2: Traffic light that cycles colours.
class TrafficLight:
    def __init__(self):
        self.colour = "red"

    def show(self):
        print(f"Current light: {self.colour}")

    def next_light(self):
        # Simple mapping: each colour points to the next one.
        sequence = {"red": "green", "green": "yellow", "yellow": "red"}
        self.colour = sequence[self.colour]
        print(self.colour)

light = TrafficLight()
light.show()        # red
light.next_light()  # green
light.next_light()  # yellow
light.next_light()  # red
light.next_light()  # green


# EXERCISE 3: ShoppingCart that builds up a list.
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})

    def total(self):
        # Sum the "price" field of every dict in self.items.
        total = 0
        for item in self.items:
            total += item["price"]
        return total

    def receipt(self):
        print("--- Receipt ---")
        for item in self.items:
            print(f"{item['name']:<10} Rs. {item['price']}")
        print(f"{'Total':<10} Rs. {self.total()}")

cart = ShoppingCart()
cart.add_item("Apple", 20)
cart.add_item("Bread", 35)
cart.add_item("Milk", 25)
cart.receipt()


# EXERCISE 4: Rectangle — methods that CALL other methods.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def describe(self):
        print(f"Rectangle {self.width}×{self.height}")
        print(f"  Area:      {self.area()}")
        print(f"  Perimeter: {self.perimeter()}")
        print(f"  Square?:   {self.is_square()}")

for r in (Rectangle(4, 6), Rectangle(5, 5), Rectangle(10, 3)):
    r.describe()
