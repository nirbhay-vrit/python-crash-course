# ---------------------------------------------------------
# DAY 6 | TOPIC 4: FUNCTIONS CALLING FUNCTIONS 🔧
# Big problems are easier when you break them into small helpers.
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: THE PROBLEM WITH ONE BIG FUNCTION
# ─────────────────────────────────────────────────────────
# Imagine you want to print a full student report.
# You COULD cram everything into one function...

def print_full_report_BAD(name, scores):
    total = 0
    for s in scores:
        total += s
    average = total / len(scores)
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    else:
        grade = "F"
    print("=" * 30)
    print(f"  Student: {name}")
    print(f"  Average: {average:.1f}")
    print(f"  Grade:   {grade}")
    print("=" * 30)

# This works but it's hard to read, test, or reuse any part.
# If the grading rules change, you dig through a wall of code.


# ─────────────────────────────────────────────────────────
# SECTION 2: ONE JOB PER FUNCTION
# ─────────────────────────────────────────────────────────
# The better approach: each function does ONE small job.
# Then a "coordinator" function calls them all in order.

def calculate_average(scores):
    return sum(scores) / len(scores)

def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    else:
        return "F"

def print_report(name, average, grade):
    print("=" * 30)
    print(f"  Student: {name}")
    print(f"  Average: {average:.1f}")
    print(f"  Grade:   {grade}")
    print("=" * 30)

# The coordinator — it just calls the helpers:
def show_student_report(name, scores):
    avg   = calculate_average(scores)
    grade = get_letter_grade(avg)
    print_report(name, avg, grade)

print("--- Student reports ---")
show_student_report("Alice", [92, 88, 95, 90])
show_student_report("Bob",   [65, 72, 58, 70])


# ─────────────────────────────────────────────────────────
# SECTION 3: REUSING YOUR HELPERS ELSEWHERE
# ─────────────────────────────────────────────────────────
# Now those small functions can be used in OTHER places too.
# calculate_average and get_letter_grade are completely reusable.

scores_list = [78, 85, 60, 92, 55]

print("\n--- Reusing helpers ---")
avg = calculate_average(scores_list)
print(f"Class average: {avg:.1f}")
print(f"Class grade:   {get_letter_grade(avg)}")


# ─────────────────────────────────────────────────────────
# SECTION 4: FUNCTIONS THAT BUILD ON EACH OTHER
# ─────────────────────────────────────────────────────────
# Functions can form a chain — each one calling the next.

def celsius_to_kelvin(c):
    return c + 273.15

def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def temperature_report(city, celsius):
    fahrenheit = celsius_to_fahrenheit(celsius)
    kelvin     = celsius_to_kelvin(celsius)
    print(f"{city}: {celsius}°C = {fahrenheit:.1f}°F = {kelvin:.2f}K")

print("\n--- Temperature chain ---")
temperature_report("London",  15)
temperature_report("Phoenix", 42)
temperature_report("Reykjavik", -5)


# ─────────────────────────────────────────────────────────
# SECTION 5: THE "DRIVER" PATTERN
# ─────────────────────────────────────────────────────────
# In real programs, you often have a main() or run() function
# that is the "driver" — it calls other functions in order.
# This keeps your code organised and easy to follow.

def get_items():
    return ["apple", "banana", "cherry", "date", "elderberry"]

def filter_long_names(items, min_length=6):
    result = []
    for item in items:
        if len(item) >= min_length:
            result.append(item)
    return result

def capitalise_all(items):
    result = []
    for item in items:
        result.append(item.capitalize())
    return result

def display(items, title="Results"):
    print(f"\n{title}:")
    for item in items:
        print(f"  • {item}")

def run():
    items   = get_items()
    long    = filter_long_names(items)
    pretty  = capitalise_all(long)
    display(pretty, title="Long fruit names")

print("\n--- Driver pattern ---")
run()


# ─────────────────────────────────────────────────────────
# SECTION 6: TESTING HELPERS IN ISOLATION
# ─────────────────────────────────────────────────────────
# The best part of small functions: you can test each one alone,
# without running the whole program!

print("\n--- Testing helpers in isolation ---")
print(calculate_average([100, 0]))      # 50.0
print(get_letter_grade(100))            # A
print(get_letter_grade(75))             # C
print(get_letter_grade(40))             # F
print(celsius_to_fahrenheit(100))       # 212.0
print(celsius_to_kelvin(0))             # 273.15
