# ---------------------------------------------------------
# SOLUTION 2: POLYMORPHISM
# ---------------------------------------------------------
# Polymorphism = "many forms". Different classes can offer the SAME method
# name, but each does its own thing. Caller doesn't care about the type.


# EXERCISE 1: Animals that speak() differently.
class Cow:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} says: Moo!")


class Duck:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} says: Quack!")


class Lion:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} says: Roar!")


animals = [Cow("Bessie"), Duck("Donald"), Lion("Simba")]
for a in animals:
    a.speak()           # same call, different behaviours — that's polymorphism


# EXERCISE 2: Shared method overridden in subclasses.
class Instrument:
    def play(self):
        print("Playing an instrument.")


class Guitar(Instrument):
    def play(self):
        print("Strumming the guitar: dun dun dun!")


class Piano(Instrument):
    def play(self):
        print("Playing piano: do re mi...")


class Drums(Instrument):
    def play(self):
        print("Beating the drums: boom boom bap!")


def perform(instrument):
    instrument.play()   # doesn't care WHICH subclass — just that it has play()


perform(Guitar())
perform(Piano())
perform(Drums())


# EXERCISE 3: Duck typing — "if it walks like a duck and quacks like a duck..."
# No shared parent class needed. Python only cares that the method exists.
class Robot:
    def greet(self):
        print("Beep boop! I am a robot.")


class Human:
    def greet(self):
        print("Hi! Nice to meet you.")


class Alien:
    def greet(self):
        print("Greetings, Earthling!")


def introduce(entity):
    entity.greet()


for entity in [Robot(), Human(), Alien()]:
    introduce(entity)


# EXERCISE 4: Polymorphism + return values (discount strategies).
class Discount:
    def __init__(self, original_price):
        self.original_price = original_price

    def apply(self):
        return self.original_price          # default: no discount


class PercentDiscount(Discount):
    def __init__(self, original_price, percent):
        super().__init__(original_price)
        self.percent = percent

    def apply(self):
        return self.original_price * (1 - self.percent / 100)


class FlatDiscount(Discount):
    def __init__(self, original_price, flat):
        super().__init__(original_price)
        self.flat = flat

    def apply(self):
        # min 0 so we never go negative
        return max(0, self.original_price - self.flat)


class NoDiscount(Discount):
    def apply(self):
        return self.original_price


def checkout(discount_obj):
    print(f"Final price: ${discount_obj.apply():.2f}")


checkout(PercentDiscount(100, 20))      # $80.00
checkout(FlatDiscount(100, 15))         # $85.00
checkout(NoDiscount(100))               # $100.00


# EXERCISE 5 (CHALLENGE): Notification system.
class Notification:
    def __init__(self, message):
        self.message = message

    def send(self):
        print(f"Sending: {self.message}")


class EmailNotification(Notification):
    def __init__(self, message, email):
        super().__init__(message)
        self.email = email

    def send(self):
        print(f"Email to {self.email}: {self.message}")


class SMSNotification(Notification):
    def __init__(self, message, phone):
        super().__init__(message)
        self.phone = phone

    def send(self):
        print(f"SMS to {self.phone}: {self.message}")


class PushNotification(Notification):
    def __init__(self, message, device):
        super().__init__(message)
        self.device = device

    def send(self):
        print(f"Push to {self.device}: {self.message}")


def broadcast(notifications):
    for n in notifications:
        n.send()        # polymorphism in action


broadcast([
    EmailNotification("Welcome!", "alice@example.com"),
    SMSNotification("OTP: 1234", "+9779800000000"),
    PushNotification("New like!", "iPhone-12"),
])
