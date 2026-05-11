# ---------------------------------------------------------
# SOLUTION 4: DEFAULT PARAMETERS 🎯
# ---------------------------------------------------------
# A default parameter gets used if the caller didn't supply that argument.


# TASK 1: Greeting with a default.
def welcome(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

welcome("Sam")                  # uses default → "Hello, Sam!"
welcome("Sam", "Hi")            # overrides    → "Hi, Sam!"
welcome("Sam", "Good morning")  # overrides    → "Good morning, Sam!"


# TASK 2: Power function — default exponent is 2.
def power(base, exponent=2):
    return base ** exponent

print(power(3))                 # 9   (3²)
print(power(2, 3))              # 8   (2³)
print(power(5, 0))              # 1   (anything^0 is 1)


# TASK 3: Order summary.
def order_summary(item_name, quantity=1, price_each=10.0):
    total = quantity * price_each
    return f"{quantity} x {item_name} = ${total}"

print(order_summary("pencil"))
print(order_summary("notebook", 3))
print(order_summary("pen", 5, 2.5))


# TASK 4: Safe divider.
def safe_divide(numerator, denominator=1):
    if denominator == 0:
        return "Cannot divide by zero!"
    return numerator / denominator

print(safe_divide(10, 2))       # 5.0
print(safe_divide(5, 0))        # Cannot divide by zero!
print(safe_divide(7))           # 7.0 (default denominator = 1)


# ⭐ BONUS CHALLENGE: create_profile returning a dict.
def create_profile(username, status="active", role="user"):
    return {"username": username, "status": status, "role": role}

print(create_profile("alice"))
print(create_profile("bob", status="inactive"))
print(create_profile("carol", role="admin"))
print(create_profile("dave", status="banned", role="moderator"))
