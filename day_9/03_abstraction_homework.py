# ---------------------------------------------------------
# DAY 9 | HOMEWORK 3: ABSTRACTION
# ---------------------------------------------------------
# Instructions:
#   - Replace each  pass  or  # TODO  with your solution.
#   - Import ABC and abstractmethod where needed.
#   - Run the file — there should be no errors.
# ---------------------------------------------------------

from abc import ABC, abstractmethod


# ─────────────────────────────────────────────────────────
# EXERCISE 1: Your first abstract class
# ─────────────────────────────────────────────────────────
# Create an abstract class `Animal` with:
#   - __init__(self, name)
#   - abstract method: speak(self)
#   - regular method: describe(self) → prints "<name> says: <speak()>"
#
# Create two concrete subclasses:
#   Dog → speak() returns "Woof!"
#   Cat → speak() returns "Meow!"
#
# Test: create one Dog and one Cat, call describe() on each.
# Expected:
#   Rex says: Woof!
#   Luna says: Meow!

class Animal(ABC):
    pass    # TODO

class Dog(Animal):
    pass    # TODO

class Cat(Animal):
    pass    # TODO

# TODO: test


# ─────────────────────────────────────────────────────────
# EXERCISE 2: Can you instantiate an abstract class?
# ─────────────────────────────────────────────────────────
# Try to instantiate Animal directly.
# Wrap it in a try/except to catch the TypeError and print:
#   "Cannot create Animal directly: <error message>"

# TODO: use try/except to show this fails gracefully


# ─────────────────────────────────────────────────────────
# EXERCISE 3: Abstract class with multiple methods
# ─────────────────────────────────────────────────────────
# Create an abstract class `StorageDevice` with:
#   - abstract methods: save(filename, data)
#                       load(filename)
#                       delete(filename)
#   - regular method:   info() → prints "Storage device ready."
#
# Create two concrete subclasses:
#   HardDrive:
#     save   → prints "HDD: Saving <data> to <filename>"
#     load   → prints "HDD: Loading <filename>"
#     delete → prints "HDD: Deleting <filename>"
#
#   CloudStorage:
#     save   → prints "Cloud: Uploading <filename>"
#     load   → prints "Cloud: Downloading <filename>"
#     delete → prints "Cloud: Removing <filename> from cloud"
#
# Write a function use_storage(device) that:
#   calls info(), save("report.txt", "hello"), load("report.txt"),
#   and delete("report.txt").
#
# Call use_storage with one of each.

class StorageDevice(ABC):
    pass    # TODO

class HardDrive(StorageDevice):
    pass    # TODO

class CloudStorage(StorageDevice):
    pass    # TODO

def use_storage(device):
    pass    # TODO

# TODO: test with HardDrive() and CloudStorage()


# ─────────────────────────────────────────────────────────
# EXERCISE 4: Combining abstraction + polymorphism
# ─────────────────────────────────────────────────────────
# Create an abstract class `Report` with:
#   - abstract method: generate(self) → returns a string
#   - regular method:  export(self) → prints "Exporting: <generate()>"
#
# Subclasses:
#   SalesReport   → generate() returns "Sales Report: $12,400 this month"
#   StockReport   → generate() returns "Stock Report: 240 items in inventory"
#   UserReport    → generate() returns "User Report: 530 active users"
#
# Loop over a list of all three and call export() on each.

class Report(ABC):
    pass    # TODO

class SalesReport(Report):
    pass    # TODO

class StockReport(Report):
    pass    # TODO

class UserReport(Report):
    pass    # TODO

# TODO: create a list and loop, calling export()


# ─────────────────────────────────────────────────────────
# EXERCISE 5 (CHALLENGE): Plugin system
# ─────────────────────────────────────────────────────────
# Build a simple plugin system for a text editor.
#
# Abstract class `Plugin`:
#   - abstract methods: on_open(filename)
#                       on_save(filename)
#                       on_close(filename)
#   - regular property: name — must be overridden as a class variable
#
# Concrete plugins:
#   SpellChecker:
#     name = "Spell Checker"
#     on_open  → "SpellChecker: scanning <filename> for errors..."
#     on_save  → "SpellChecker: rechecking <filename>..."
#     on_close → "SpellChecker: clearing cache for <filename>."
#
#   AutoSaver:
#     name = "Auto Saver"
#     on_open  → "AutoSaver: monitoring <filename>..."
#     on_save  → "AutoSaver: backup saved for <filename>."
#     on_close → "AutoSaver: stopped monitoring <filename>."
#
# Write a class TextEditor that:
#   - stores a list of plugins
#   - has register(plugin)
#   - has open_file(filename) → calls on_open on all plugins
#   - has save_file(filename) → calls on_save on all plugins
#   - has close_file(filename) → calls on_close on all plugins
#
# Test by registering both plugins, then opening, saving, and closing a file.

class Plugin(ABC):
    pass    # TODO

class SpellChecker(Plugin):
    name = "Spell Checker"
    pass    # TODO

class AutoSaver(Plugin):
    name = "Auto Saver"
    pass    # TODO

class TextEditor:
    pass    # TODO

# TODO: create editor, register both plugins, test all three file operations
