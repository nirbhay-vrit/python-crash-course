# ---------------------------------------------------------
# SOLUTION 3: **kwargs 🗝️
# ---------------------------------------------------------
# **kwargs collects any number of KEYWORD arguments into a dictionary.


# TASK 1: Print profile in aligned format.
def print_profile(**kwargs):
    for key, value in kwargs.items():
        # :<6 means "left-align this in a 6-character-wide column"
        print(f"{key:<6} : {value}")

print_profile(name="Alice", age=30, job="Engineer", city="Paris")


# TASK 2: Make a tag — HTML-style.
def make_tag(tag_name, **attrs):
    # Build a string like:  key="value" key2="value2"
    attr_string = " ".join(f'{k}="{v}"' for k, v in attrs.items())
    if attr_string:
        print(f"<{tag_name} {attr_string}>")
    else:
        print(f"<{tag_name}>")

make_tag("a", href="https://python.org", target="_blank")
make_tag("img", src="logo.png", alt="Logo")


# TASK 3: Merge two dictionaries — second wins on conflict.
def merge(d1, d2):
    return {**d1, **d2}         # ** unpacks each dict into the new one

base = {"color": "blue", "size": "M", "material": "cotton"}
updates = {"color": "red", "size": "L"}
print(merge(base, updates))     # color=red, size=L, material=cotton


# TASK 4: Flexible introduction.
def introduce(name, **kwargs):
    print(f"Hi, I'm {name}.")
    for key, value in kwargs.items():
        print(f"My {key} is {value}.")

introduce("Bob", age=25, job="developer", hobby="chess")


# ⭐ BONUS CHALLENGE: summarise — mix *args and **kwargs.
def summarise(*args, **kwargs):
    print(f"Sum of numbers: {sum(args)}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

summarise(10, 20, 30, name="Alice", grade="A")
