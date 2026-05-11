# ---------------------------------------------------------
# SOLUTION 5: RECURSION 🔁
# ---------------------------------------------------------
# A recursive function calls ITSELF on a smaller problem,
# until it hits a BASE CASE (a tiny problem it can answer directly).


# TASK 1: Count up — recursive call BEFORE the print.
def count_up(n):
    if n <= 0:                  # base case: stop counting
        return
    count_up(n - 1)             # do the smaller problem first
    print(n)                    # then print this number on the way "back up"

count_up(5)                     # prints 1, 2, 3, 4, 5


# TASK 2: Sum of digits.
def sum_digits(n):
    if n < 10:                  # base case: single digit
        return n
    return (n % 10) + sum_digits(n // 10)
    # n % 10  = last digit
    # n // 10 = the rest of the number with the last digit chopped off

print(sum_digits(123))          # 6
print(sum_digits(9))            # 9
print(sum_digits(9876))         # 30


# TASK 3: Repeat a string with recursion (no * operator).
def repeat(text, times):
    if times <= 0:
        return ""               # base case
    return text + repeat(text, times - 1)

print(repeat("hi", 3))          # hihihi
print(repeat("hi", 0))          # ""


# TASK 4: Fibonacci.
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

for i in range(9):              # fib(0)..fib(8)
    print(f"fib({i}) = {fib(i)}")


# ⭐ BONUS CHALLENGE: Flatten a nested list.
def flatten(items):
    if not items:               # base case: empty list
        return []
    first = items[0]
    rest = items[1:]
    if isinstance(first, list):
        # first is itself a list → flatten IT, then concat with the rest flattened
        return flatten(first) + flatten(rest)
    # first is a regular item → put it first, then flatten the rest
    return [first] + flatten(rest)

print(flatten([1, [2, 3], [4, [5, 6]]]))            # [1, 2, 3, 4, 5, 6]
print(flatten([[1, [2]], 3, [[[4]]], 5]))           # [1, 2, 3, 4, 5]
