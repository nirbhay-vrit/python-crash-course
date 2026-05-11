# ---------------------------------------------------------
# SOLUTION 3: ABSTRACTION
# ---------------------------------------------------------
# An abstract class is a TEMPLATE — you can't instantiate it.
# Subclasses MUST implement every @abstractmethod, or Python won't let
# you create them. Great for enforcing a consistent interface.

from abc import ABC, abstractmethod


# EXERCISE 1: First abstract class.
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass        # subclasses MUST override this

    def describe(self):
        # `speak()` will dispatch to the subclass's version.
        print(f"{self.name} says: {self.speak()}")


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


Dog("Rex").describe()       # Rex says: Woof!
Cat("Luna").describe()      # Luna says: Meow!


# EXERCISE 2: Trying to instantiate an abstract class fails.
try:
    a = Animal("Generic")
except TypeError as e:
    print(f"Cannot create Animal directly: {e}")


# EXERCISE 3: Abstract class with multiple methods.
class StorageDevice(ABC):
    @abstractmethod
    def save(self, filename, data):
        pass

    @abstractmethod
    def load(self, filename):
        pass

    @abstractmethod
    def delete(self, filename):
        pass

    def info(self):
        print("Storage device ready.")


class HardDrive(StorageDevice):
    def save(self, filename, data):
        print(f"HDD: Saving {data} to {filename}")

    def load(self, filename):
        print(f"HDD: Loading {filename}")

    def delete(self, filename):
        print(f"HDD: Deleting {filename}")


class CloudStorage(StorageDevice):
    def save(self, filename, data):
        print(f"Cloud: Uploading {filename}")

    def load(self, filename):
        print(f"Cloud: Downloading {filename}")

    def delete(self, filename):
        print(f"Cloud: Removing {filename} from cloud")


def use_storage(device):
    device.info()
    device.save("report.txt", "hello")
    device.load("report.txt")
    device.delete("report.txt")


use_storage(HardDrive())
print()
use_storage(CloudStorage())


# EXERCISE 4: Abstraction + polymorphism.
class Report(ABC):
    @abstractmethod
    def generate(self):
        pass

    def export(self):
        print(f"Exporting: {self.generate()}")


class SalesReport(Report):
    def generate(self):
        return "Sales Report: $12,400 this month"


class StockReport(Report):
    def generate(self):
        return "Stock Report: 240 items in inventory"


class UserReport(Report):
    def generate(self):
        return "User Report: 530 active users"


print()
for r in [SalesReport(), StockReport(), UserReport()]:
    r.export()


# EXERCISE 5 (CHALLENGE): Plugin system.
class Plugin(ABC):
    name = "Unnamed Plugin"     # subclasses override this as a class variable

    @abstractmethod
    def on_open(self, filename):
        pass

    @abstractmethod
    def on_save(self, filename):
        pass

    @abstractmethod
    def on_close(self, filename):
        pass


class SpellChecker(Plugin):
    name = "Spell Checker"

    def on_open(self, filename):
        print(f"SpellChecker: scanning {filename} for errors...")

    def on_save(self, filename):
        print(f"SpellChecker: rechecking {filename}...")

    def on_close(self, filename):
        print(f"SpellChecker: clearing cache for {filename}.")


class AutoSaver(Plugin):
    name = "Auto Saver"

    def on_open(self, filename):
        print(f"AutoSaver: monitoring {filename}...")

    def on_save(self, filename):
        print(f"AutoSaver: backup saved for {filename}.")

    def on_close(self, filename):
        print(f"AutoSaver: stopped monitoring {filename}.")


class TextEditor:
    def __init__(self):
        self.plugins = []

    def register(self, plugin):
        self.plugins.append(plugin)
        print(f"Registered plugin: {plugin.name}")

    def open_file(self, filename):
        print(f"\n[Opening {filename}]")
        for p in self.plugins:
            p.on_open(filename)

    def save_file(self, filename):
        print(f"\n[Saving {filename}]")
        for p in self.plugins:
            p.on_save(filename)

    def close_file(self, filename):
        print(f"\n[Closing {filename}]")
        for p in self.plugins:
            p.on_close(filename)


editor = TextEditor()
editor.register(SpellChecker())
editor.register(AutoSaver())

editor.open_file("notes.txt")
editor.save_file("notes.txt")
editor.close_file("notes.txt")
