# ---------------------------------------------------------
# SOLUTION 2: *args ✳️
# ---------------------------------------------------------
# *args collects any number of POSITIONAL arguments into a tuple,
# so a function can accept "as many" values as you want.


# TASK 1: my_sum — add any number of numbers.
def my_sum(*args):
    total = 0
    for n in args:              # args is a tuple — loop through it
        total += n
    return total

print(my_sum(1, 2))             # 3
print(my_sum(5, 10, 15))        # 30
print(my_sum(1, 2, 3, 4, 5))    # 15


# TASK 2: print_all — label + variable items.
def print_all(label, *items):
    print(f"{label}:")
    for item in items:
        print(f"- {item}")

print_all("Fruits", "apple", "mango", "banana")


# TASK 3: Longest string.
def longest(*words):
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

print(longest("cat", "elephant", "dog", "hippopotamus"))


# TASK 4: Above average.
def above_average(*numbers):
    if not numbers:
        return                  # nothing to compare
    average = sum(numbers) / len(numbers)
    print(f"Average is {average}")
    for n in numbers:
        if n > average:
            print(n)

above_average(4, 8, 15, 16, 23, 42)


# ⭐ BONUS CHALLENGE: multiply each, then sum.
def multiply_then_add(multiplier, *values):
    total = 0
    for v in values:
        total += v * multiplier
    return total

print(multiply_then_add(2, 1, 2, 3))    # 2*1 + 2*2 + 2*3 = 12
