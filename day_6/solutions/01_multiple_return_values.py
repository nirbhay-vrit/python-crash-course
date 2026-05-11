# ---------------------------------------------------------
# SOLUTION 1: MULTIPLE RETURN VALUES 🎁
# ---------------------------------------------------------
# Python lets you `return a, b, c` — it bundles them into a tuple.
# You can "unpack" them at the call site: x, y, z = my_func(...)


# TASK 1: Count evens and odds.
def split_even_odd(numbers):
    evens = 0
    odds = 0
    for n in numbers:
        if n % 2 == 0:
            evens += 1
        else:
            odds += 1
    return evens, odds          # returns a tuple (evens, odds)

e, o = split_even_odd([1, 2, 3, 4, 5, 6, 7, 8])
print(f"{e} even, {o} odd")


# TASK 2: Name splitter.
def split_full_name(full_name):
    parts = full_name.split(" ", 1)   # split on the first space only
    first = parts[0]
    last = parts[1] if len(parts) > 1 else ""
    return first, last

first, last = split_full_name("Ada Lovelace")
print(f"First: {first}, Last: {last}")


# TASK 3: Grade stats.
def grade_stats(grades):
    average = sum(grades) / len(grades)
    return average, max(grades), min(grades)

avg, hi, lo = grade_stats([78, 95, 62, 88, 71])
print(f"Average: {avg}, Highest: {hi}, Lowest: {lo}")


# TASK 4: Celsius converter — return two values.
def convert_temperature(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin

for c in [0, 100, -40]:
    f, k = convert_temperature(c)
    print(f"{c}°C → {f}°F, {k}K")


# ⭐ BONUS CHALLENGE: stats returning 5 values.
def stats(numbers):
    count = len(numbers)
    total = sum(numbers)
    return min(numbers), max(numbers), total, total / count, count

lo, hi, total, avg, count = stats([4, 8, 15, 16, 23, 42])
print("\n----- REPORT -----")
print(f"Count:   {count}")
print(f"Min:     {lo}")
print(f"Max:     {hi}")
print(f"Sum:     {total}")
print(f"Average: {avg}")
