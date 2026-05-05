# ---------------------------------------------------------
# DAY 7 | REVISION 4: FUNCTIONS — Everything in One Place
# Day 5 and 6 taught functions. Today we revise all of it.
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: WHY FUNCTIONS EXIST
# ─────────────────────────────────────────────────────────
# Problem: Without functions, you repeat the same code.
# Solution: Write it ONCE, use it anywhere.

# WITHOUT a function (messy):
name1 = "Alice"
print(f"Hello, {name1}! Welcome.")
print(f"We are glad you are here, {name1}.")

name2 = "Bob"
print(f"Hello, {name2}! Welcome.")
print(f"We are glad you are here, {name2}.")

# That's 4 lines for 2 people. 100 people = 200 lines!

# WITH a function (clean):
def greet(name):
    print(f"Hello, {name}! Welcome.")
    print(f"We are glad you are here, {name}.")

print("\n--- Using the function ---")
greet("Alice")
greet("Bob")
greet("Charlie")   # one line per person, no matter how many!


# ─────────────────────────────────────────────────────────
# SECTION 2: ANATOMY OF A FUNCTION
# ─────────────────────────────────────────────────────────
#
#   def  function_name  (parameter):
#        ↑ keyword        ↑ input
#       tells Python
#       "define a function"
#
#       [indented body — the code that runs when called]
#
#   function_name(argument)   ← calling/using the function
#
# def  → defines the function (writes the recipe)
# call → actually runs it (cooks the dish)

def say_hello():           # no parameters — takes no input
    print("Hello!")

print("\n--- Calling a simple function ---")
say_hello()               # call it
say_hello()               # call it again — runs twice!


# ─────────────────────────────────────────────────────────
# SECTION 3: PARAMETERS — Giving the function input
# ─────────────────────────────────────────────────────────
# A parameter is the variable inside the def line.
# An argument is the actual value you pass when calling.

def add(a, b):             # a and b are PARAMETERS
    result = a + b
    print(f"{a} + {b} = {result}")

print("\n--- Parameters and arguments ---")
add(3, 4)                  # 3 and 4 are ARGUMENTS → a=3, b=4
add(10, 20)                # a=10, b=20
add(100, 5)                # a=100, b=5


# ─────────────────────────────────────────────────────────
# SECTION 4: RETURN — Getting a result back
# ─────────────────────────────────────────────────────────
# print() just SHOWS a value. return SENDS it back.
# Use return when you need to USE the result later.

def multiply(a, b):
    return a * b           # sends the result back to the caller

print("\n--- Return values ---")
answer = multiply(6, 7)    # the return value is stored in 'answer'
print(answer)              # 42

# You can use the return value directly:
print(multiply(3, 3))      # 9


# ─────────────────────────────────────────────────────────
# SECTION 5: print vs return — The key difference
# ─────────────────────────────────────────────────────────

def square_print(n):
    print(n * n)            # just shows it — cannot save or use it

def square_return(n):
    return n * n            # sends it back — can save and use it

print("\n--- print vs return ---")
square_print(5)             # shows 25, but you can't save it

result = square_return(5)   # save 25
doubled = result * 2        # use it: 50
print(f"25 doubled is {doubled}")

# Rule of thumb: if you need to DO something with the result later,
# use return. If you just want to see it, use print.


# ─────────────────────────────────────────────────────────
# SECTION 6: DEFAULT PARAMETERS
# ─────────────────────────────────────────────────────────
# A default value is used when the caller doesn't pass one.

def greet_user(name, greeting="Hello"):     # greeting has a default
    print(f"{greeting}, {name}!")

print("\n--- Default parameters ---")
greet_user("Alice")                # uses default "Hello"
greet_user("Bob", "Good morning")  # overrides the default
greet_user("Charlie", "Hey")       # overrides again


# ─────────────────────────────────────────────────────────
# SECTION 7: KEYWORD ARGUMENTS
# ─────────────────────────────────────────────────────────
# You can pass arguments by NAME so order doesn't matter.

def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")

print("\n--- Keyword arguments ---")
describe_pet("dog", "Rex")                    # positional (order matters)
describe_pet(name="Whiskers", animal="cat")   # keyword (order doesn't matter)


# ─────────────────────────────────────────────────────────
# SECTION 8: SCOPE — Local vs Global
# ─────────────────────────────────────────────────────────
# Variables INSIDE a function are LOCAL — they only exist there.
# Variables OUTSIDE are GLOBAL — they exist everywhere.

global_var = "I am global"

def show_scope():
    local_var = "I am local"   # only exists inside this function
    print(global_var)          # can READ global from inside
    print(local_var)

print("\n--- Scope ---")
show_scope()
print(global_var)              # fine — global exists everywhere
# print(local_var)             # ← ERROR: local_var doesn't exist out here


# ─────────────────────────────────────────────────────────
# SECTION 9: FUNCTIONS INSIDE LOOPS — Super useful combo!
# ─────────────────────────────────────────────────────────
# Define a function ONCE, then call it inside a loop.

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "F"

print("\n--- Function called inside a loop ---")
student_scores = [88, 95, 62, 45, 73, 91]

for score in student_scores:
    grade = get_grade(score)
    print(f"Score: {score}  →  Grade: {grade}")


# ─────────────────────────────────────────────────────────
# SECTION 10: PUTTING IT ALL TOGETHER
# ─────────────────────────────────────────────────────────
# A mini program using: function, loop, return, default param

def make_badge(name, role="Student"):
    return f"[ {name.upper()} | {role} ]"

def print_badges(people):
    print("\n--- BADGES ---")
    for person in people:
        badge = make_badge(person["name"], person.get("role", "Student"))
        print(badge)

attendees = [
    {"name": "Alice"},
    {"name": "Bob",     "role": "Mentor"},
    {"name": "Charlie"},
    {"name": "Diana",   "role": "Teacher"},
]

print_badges(attendees)
