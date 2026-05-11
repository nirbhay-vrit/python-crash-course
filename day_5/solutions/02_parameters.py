# ---------------------------------------------------------
# SOLUTION 2: PARAMETERS 📬
# ---------------------------------------------------------
# Parameters are "slots" in the function definition.
# Arguments are the values you pass IN when calling.


# TASK 1: Personalised greeting.
def greet_user(username):
    print(f"Hello, {username}! Great to see you today.")

greet_user("Alice")
greet_user("Bob")
greet_user("Charlie")


# TASK 2: Rectangle info — two parameters.
def describe_rectangle(width, height):
    area = width * height
    print(f"Width: {width}, Height: {height}, Area: {area}")

describe_rectangle(5, 3)
describe_rectangle(10, 2)
describe_rectangle(7, 7)


# TASK 3: Temperature checker.
def check_temperature(temp):
    if temp > 37:
        print("Too hot! 🔥")
    elif temp < 36:
        print("Too cold! 🥶")
    else:
        print("Normal temperature. 😊")

check_temperature(38)
check_temperature(35)
check_temperature(36.5)


# ⭐ BONUS CHALLENGE: Print n stars.
def print_stars(n):
    print("*" * n)              # string * number repeats it

print_stars(1)
print_stars(3)
print_stars(5)
print_stars(7)
