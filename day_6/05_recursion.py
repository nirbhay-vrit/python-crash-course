# ---------------------------------------------------------
# DAY 6 | TOPIC 5: RECURSION 🔁
# A function that calls ITSELF — with a stopping condition!
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: WHAT IS RECURSION?
# ─────────────────────────────────────────────────────────
# Recursion means a function solves a problem by calling ITSELF
# on a SMALLER version of the same problem.
#
# Every recursive function needs TWO things:
#   1. BASE CASE   — the condition to STOP (otherwise it runs forever!)
#   2. RECURSIVE CASE — the function calls itself on a smaller input
#
# Think of it like Russian dolls: each doll contains a smaller one
# until you reach the tiniest one — that's the base case.

# Here is the SIMPLEST possible recursive function:

def countdown(n):
    if n <= 0:           # BASE CASE — stop here!
        print("Go!")
        return
    print(n)
    countdown(n - 1)     # RECURSIVE CASE — call with a smaller n

print("--- Countdown ---")
countdown(5)


# ─────────────────────────────────────────────────────────
# SECTION 2: TRACING WHAT HAPPENS
# ─────────────────────────────────────────────────────────
# Let's add indentation to visualise the call stack.

def countdown_trace(n, depth=0):
    indent = "  " * depth
    print(f"{indent}countdown({n}) called")
    if n <= 0:
        print(f"{indent}→ BASE CASE: returning")
        return
    countdown_trace(n - 1, depth + 1)
    print(f"{indent}← back in countdown({n})")

print("\n--- Trace of countdown(3) ---")
countdown_trace(3)


# ─────────────────────────────────────────────────────────
# SECTION 3: FACTORIAL — CLASSIC RECURSION
# ─────────────────────────────────────────────────────────
# 5! = 5 × 4 × 3 × 2 × 1 = 120
#
# Notice the pattern:
#   5! = 5 × 4!
#   4! = 4 × 3!
#   3! = 3 × 2!
#   2! = 2 × 1!
#   1! = 1         ← base case
#
# In words: factorial(n) = n × factorial(n - 1)

def factorial(n):
    if n == 1:                      # BASE CASE
        return 1
    return n * factorial(n - 1)    # RECURSIVE CASE

print("\n--- Factorial ---")
print(f"3! = {factorial(3)}")    # 6
print(f"5! = {factorial(5)}")    # 120
print(f"6! = {factorial(6)}")    # 720


# ─────────────────────────────────────────────────────────
# SECTION 4: SUM OF A LIST
# ─────────────────────────────────────────────────────────
# sum([3, 1, 4, 1, 5])
# = 3 + sum([1, 4, 1, 5])
# = 3 + 1 + sum([4, 1, 5])
# = ... until the list is empty → return 0 (base case)

def my_sum(numbers):
    if len(numbers) == 0:           # BASE CASE — empty list
        return 0
    return numbers[0] + my_sum(numbers[1:])   # first + sum of rest

print("\n--- Sum of list recursively ---")
print(my_sum([3, 1, 4, 1, 5]))    # 14
print(my_sum([10, 20, 30]))        # 60
print(my_sum([]))                  # 0


# ─────────────────────────────────────────────────────────
# SECTION 5: RECURSION VS LOOP — SAME RESULT, DIFFERENT STYLE
# ─────────────────────────────────────────────────────────
# Almost anything you do with recursion can also be done with a loop.
# Loops are usually more efficient; recursion is sometimes more readable.

def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n == 1:
        return 1
    return n * factorial_recursive(n - 1)

print("\n--- Loop vs Recursive factorial ---")
for n in [1, 3, 5, 7]:
    loop_result = factorial_loop(n)
    rec_result  = factorial_recursive(n)
    match = "✅" if loop_result == rec_result else "❌"
    print(f"  {n}! loop={loop_result}  recursive={rec_result}  {match}")


# ─────────────────────────────────────────────────────────
# SECTION 6: THE GOLDEN RULE — ALWAYS HAVE A BASE CASE
# ─────────────────────────────────────────────────────────
# Without a base case, recursion never stops and Python raises:
#   RecursionError: maximum recursion depth exceeded
#
# Always ask yourself BEFORE writing recursive code:
#   "What is the SIMPLEST version of this problem?"
#   "When should the function STOP calling itself?"

def power(base, exp):
    if exp == 0:              # BASE CASE: anything to the power 0 is 1
        return 1
    return base * power(base, exp - 1)

print("\n--- Power function ---")
print(f"2^0  = {power(2, 0)}")    # 1
print(f"2^3  = {power(2, 3)}")    # 8
print(f"3^4  = {power(3, 4)}")    # 81
print(f"10^2 = {power(10, 2)}")   # 100
