# ---------------------------------------------------------
# DAY 9 | HOMEWORK 2: POLYMORPHISM
# ---------------------------------------------------------
# Instructions:
#   - Replace each  pass  or  # TODO  with your solution.
#   - Run the file — there should be no errors.
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# EXERCISE 1: Basic polymorphism — speak()
# ─────────────────────────────────────────────────────────
# Create three classes: Cow, Duck, Lion.
# Each has __init__(self, name) and a speak() method.
#   Cow  → "<name> says: Moo!"
#   Duck → "<name> says: Quack!"
#   Lion → "<name> says: Roar!"
#
# Then loop over a list of mixed animals and call speak() on each.
# Expected output (with these names):
#   Bessie says: Moo!
#   Donald says: Quack!
#   Simba says: Roar!

class Cow:
    pass    # TODO

class Duck:
    pass    # TODO

class Lion:
    pass    # TODO

# TODO: create a list [Cow("Bessie"), Duck("Donald"), Lion("Simba")]
# and loop, calling speak() on each.


# ─────────────────────────────────────────────────────────
# EXERCISE 2: Polymorphism with a shared method
# ─────────────────────────────────────────────────────────
# Create a parent class `Instrument` with a play() method
# that prints "Playing an instrument."
#
# Create three subclasses: Guitar, Piano, Drums.
# Each overrides play():
#   Guitar → "Strumming the guitar: dun dun dun!"
#   Piano  → "Playing piano: do re mi..."
#   Drums  → "Beating the drums: boom boom bap!"
#
# Write a function perform(instrument) that calls instrument.play().
# Call perform() with one of each instrument.

class Instrument:
    pass    # TODO

class Guitar(Instrument):
    pass    # TODO

class Piano(Instrument):
    pass    # TODO

class Drums(Instrument):
    pass    # TODO

def perform(instrument):
    pass    # TODO


# TODO: call perform() with one of each


# ─────────────────────────────────────────────────────────
# EXERCISE 3: Duck typing
# ─────────────────────────────────────────────────────────
# Create three unrelated classes (no shared parent):
#   Robot   — has greet() → prints "Beep boop! I am a robot."
#   Human   — has greet() → prints "Hi! Nice to meet you."
#   Alien   — has greet() → prints "Greetings, Earthling!"
#
# Write a function introduce(entity) that calls entity.greet().
# Loop over a mixed list and call introduce() on each.
# This works without inheritance — duck typing!

class Robot:
    pass    # TODO

class Human:
    pass    # TODO

class Alien:
    pass    # TODO

def introduce(entity):
    pass    # TODO

# TODO: create a list of one of each and test


# ─────────────────────────────────────────────────────────
# EXERCISE 4: Polymorphism + return values
# ─────────────────────────────────────────────────────────
# Create a parent class `Discount` with:
#   - __init__(self, original_price)
#   - apply(self)  → returns the original price (no discount)
#
# Create three subclasses:
#   PercentDiscount(original_price, percent)
#     → apply() returns price * (1 - percent/100)
#   FlatDiscount(original_price, flat)
#     → apply() returns price - flat  (min 0)
#   NoDiscount(original_price)
#     → apply() returns original price (no change)
#
# Write a function checkout(discount_obj) that prints:
#   "Final price: $<amount>"
#
# Test with:
#   checkout(PercentDiscount(100, 20))   → $80.00
#   checkout(FlatDiscount(100, 15))      → $85.00
#   checkout(NoDiscount(100))            → $100.00

class Discount:
    pass    # TODO

class PercentDiscount(Discount):
    pass    # TODO

class FlatDiscount(Discount):
    pass    # TODO

class NoDiscount(Discount):
    pass    # TODO

def checkout(discount_obj):
    pass    # TODO

# TODO: test all three


# ─────────────────────────────────────────────────────────
# EXERCISE 5 (CHALLENGE): Notification system
# ─────────────────────────────────────────────────────────
# Build a notification system:
#
# Parent class Notification:
#   - __init__(self, message)
#   - send(self)  → prints "Sending: <message>" (default)
#
# Subclasses:
#   EmailNotification(message, email)
#     → send(): "Email to <email>: <message>"
#   SMSNotification(message, phone)
#     → send(): "SMS to <phone>: <message>"
#   PushNotification(message, device)
#     → send(): "Push to <device>: <message>"
#
# Write a function broadcast(notifications) that takes a LIST
# of notification objects and calls send() on each.
#
# Test with a mixed list of all three types.

class Notification:
    pass    # TODO

class EmailNotification(Notification):
    pass    # TODO

class SMSNotification(Notification):
    pass    # TODO

class PushNotification(Notification):
    pass    # TODO

def broadcast(notifications):
    pass    # TODO

# TODO: create a mixed list and call broadcast()
