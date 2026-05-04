# ---------------------------------------------------------
# DAY 6 | TOPIC 3: **kwargs — Variable Keyword Arguments 🗝️
# Collect any number of named (keyword) arguments!
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: WHAT IS **kwargs?
# ─────────────────────────────────────────────────────────
# While *args collects positional arguments into a TUPLE,
# **kwargs collects KEYWORD arguments into a DICTIONARY.
# 'kwargs' stands for keyword arguments. The ** is what matters.

def show_profile(**kwargs):
    print(f"Type:   {type(kwargs)}")
    print(f"Values: {kwargs}")

print("--- **kwargs is a dictionary ---")
show_profile(name="Alice", age=30, city="Paris")
# Type:   <class 'dict'>
# Values: {'name': 'Alice', 'age': 30, 'city': 'Paris'}


# ─────────────────────────────────────────────────────────
# SECTION 2: LOOPING THROUGH **kwargs
# ─────────────────────────────────────────────────────────
# Since kwargs is a dict, you loop through it the same way.

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("\n--- Looping through kwargs ---")
print("Product details:")
print_info(name="Laptop", brand="TechCo", price=999, in_stock=True)


# ─────────────────────────────────────────────────────────
# SECTION 3: COMBINING POSITIONAL, *args, AND **kwargs
# ─────────────────────────────────────────────────────────
# You can use all three together. Order MUST be:
#   1. regular parameters
#   2. *args
#   3. **kwargs

def full_order(table, *items, **options):
    print(f"\nTable {table}:")
    print("  Items:", ", ".join(items))
    for option, value in options.items():
        print(f"  {option}: {value}")

print("\n--- Combined positional + *args + **kwargs ---")
full_order(5, "pizza", "salad", "juice",
           payment="card", discount=True, notes="window seat")


# ─────────────────────────────────────────────────────────
# SECTION 4: BUILDING A FLEXIBLE GREETING FUNCTION
# ─────────────────────────────────────────────────────────
# Let's use **kwargs to build a greeting that can include
# any optional extras like title, company, or language.

def greet(name, **extras):
    title   = extras.get("title", "")
    company = extras.get("company", "")

    greeting = f"Hello, {title + ' ' if title else ''}{name}"
    if company:
        greeting += f" from {company}"
    print(greeting + "!")

print("\n--- Flexible greeting ---")
greet("Alice")
greet("Bob", title="Dr")
greet("Charlie", title="Prof", company="MIT")
greet("Diana", company="Google")


# ─────────────────────────────────────────────────────────
# SECTION 5: UNPACKING A DICTIONARY WITH **
# ─────────────────────────────────────────────────────────
# Just like * unpacks a list, ** unpacks a dict as keyword args.

def create_user(username, email, role):
    print(f"User: {username} | Email: {email} | Role: {role}")

user_data = {
    "username": "nirbhay99",
    "email":    "nirbhay@example.com",
    "role":     "admin"
}

print("\n--- Unpacking a dict with ** ---")
create_user(**user_data)    # same as create_user(username=..., email=..., role=...)


# ─────────────────────────────────────────────────────────
# SECTION 6: REAL-WORLD PATTERN — CONFIG BUILDER
# ─────────────────────────────────────────────────────────
# **kwargs is commonly used for configuration or settings.

DEFAULT_CONFIG = {
    "theme":    "light",
    "language": "English",
    "font_size": 14,
}

def apply_config(base, **overrides):
    config = base.copy()      # start with defaults
    config.update(overrides)  # apply user changes on top
    return config

user_config = apply_config(DEFAULT_CONFIG, theme="dark", font_size=18)

print("\n--- Config builder ---")
for key, value in user_config.items():
    print(f"  {key}: {value}")
