# ---------------------------------------------------------
# DAY 9 | HOMEWORK 4: SPECIAL (DUNDER) METHODS
# ---------------------------------------------------------
# Instructions:
#   - Replace each  pass  or  # TODO  with your solution.
#   - Run the file — there should be no errors.
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# EXERCISE 1: Add __str__ to a class
# ─────────────────────────────────────────────────────────
# Add __str__ to the class below so that:
#   print(movie)  outputs:  "The Matrix" (1999) — Sci-Fi
#
# Do NOT change __init__.

class Movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year  = year
        self.genre = genre

    # TODO: add __str__


m = Movie("The Matrix", 1999, "Sci-Fi")
print(m)   # "The Matrix" (1999) — Sci-Fi


# ─────────────────────────────────────────────────────────
# EXERCISE 2: Add __len__ and __contains__
# ─────────────────────────────────────────────────────────
# Add __len__ and __contains__ to the Playlist class so that:
#   len(playlist)          → number of songs
#   "Bohemian Rhapsody" in playlist → True or False

class Playlist:
    def __init__(self, name):
        self.name  = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def __str__(self):
        return f"Playlist '{self.name}' — {len(self)} songs"

    # TODO: add __len__

    # TODO: add __contains__


pl = Playlist("My Favourites")
pl.add_song("Bohemian Rhapsody")
pl.add_song("Hotel California")
pl.add_song("Stairway to Heaven")

print(pl)                              # Playlist 'My Favourites' — 3 songs
print(len(pl))                         # 3
print("Hotel California" in pl)        # True
print("Shape of You" in pl)            # False


# ─────────────────────────────────────────────────────────
# EXERCISE 3: Add __eq__ for comparison
# ─────────────────────────────────────────────────────────
# Add __eq__ to Product so two products are equal
# if they have the same sku (stock-keeping unit code).

class Product:
    def __init__(self, name, sku, price):
        self.name  = name
        self.sku   = sku
        self.price = price

    def __str__(self):
        return f"{self.name} (SKU: {self.sku}, ${self.price:.2f})"

    # TODO: add __eq__ — two products are equal if same sku


p1 = Product("Widget A", "SKU-001", 9.99)
p2 = Product("Widget A Deluxe", "SKU-001", 14.99)   # same SKU!
p3 = Product("Gadget B", "SKU-002", 19.99)

print(p1 == p2)    # True  — same SKU
print(p1 == p3)    # False — different SKU


# ─────────────────────────────────────────────────────────
# EXERCISE 4: Add __add__ — operator overloading
# ─────────────────────────────────────────────────────────
# Make it possible to add two ShoppingCart objects together.
# The result is a new ShoppingCart whose items list
# is the combined items of both carts.

class ShoppingCart:
    def __init__(self, owner):
        self.owner = owner
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __str__(self):
        return f"{self.owner}'s cart: {self.items}"

    # TODO: add __add__ — returns a new ShoppingCart("merged")
    #       with items = self.items + other.items


cart1 = ShoppingCart("Alice")
cart1.add("Book")
cart1.add("Pen")

cart2 = ShoppingCart("Bob")
cart2.add("Notebook")
cart2.add("Ruler")

merged = cart1 + cart2
print(merged)   # merged's cart: ['Book', 'Pen', 'Notebook', 'Ruler']


# ─────────────────────────────────────────────────────────
# EXERCISE 5 (CHALLENGE): Full-featured Temperature class
# ─────────────────────────────────────────────────────────
# Build a Temperature class with:
#   __init__(self, celsius)
#   __str__   → "25.0°C"
#   __repr__  → "Temperature(25.0)"
#   __eq__    → True if same celsius value
#   __lt__    → True if self.celsius < other.celsius
#   __add__   → adds celsius values, returns new Temperature
#   to_fahrenheit() → returns (celsius * 9/5) + 32
#
# After implementing, ALL of these should work:

class Temperature:
    pass    # TODO


t1 = Temperature(20)
t2 = Temperature(30)
t3 = Temperature(20)

print(t1)               # 20°C
print(repr(t1))         # Temperature(20)
print(t1 == t3)         # True
print(t1 == t2)         # False
print(t1 < t2)          # True
combined = t1 + t2
print(combined)         # 50°C
print(t1.to_fahrenheit())  # 68.0

temps = [t2, t1, Temperature(25)]
for t in sorted(temps):
    print(t)            # 20°C, 25°C, 30°C
