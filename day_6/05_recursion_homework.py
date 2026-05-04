# ---------------------------------------------------------
# HOMEWORK 5: RECURSION 🔁
# ---------------------------------------------------------


# TASK 1: Count Up
# Write a recursive function called 'count_up' that takes a number n
# and prints 1, 2, 3, ... n (counting UP instead of down).
# Hint: the recursive call should happen BEFORE the print!
# Test it with count_up(5) → prints 1 2 3 4 5 on separate lines.
# Write your code below:




# TASK 2: Sum of Digits
# Write a recursive function called 'sum_digits' that takes a
# positive integer and returns the sum of its digits.
# Example: sum_digits(123) → 1 + 2 + 3 = 6
#          sum_digits(9)   → 9  (base case: single digit)
# Hint: n % 10 gives the last digit, n // 10 removes the last digit.
# Write your code below:




# TASK 3: Repeat String
# Write a recursive function called 'repeat' that takes a string
# and a number, and returns the string repeated that many times.
# Example: repeat("hi", 3) → "hihihi"
#          repeat("hi", 0) → ""  (base case)
# Do NOT use * operator — use recursion only!
# Write your code below:




# TASK 4: Fibonacci
# The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Each number is the sum of the previous two.
# fib(0) = 0  (base case)
# fib(1) = 1  (base case)
# fib(n) = fib(n-1) + fib(n-2)
# Write a recursive function 'fib(n)' and print fib(0) through fib(8).
# Write your code below:




# ⭐ BONUS CHALLENGE:
# Write a recursive function called 'flatten' that takes a nested list
# (a list that may contain other lists inside it) and returns a flat list.
# Example:
#   flatten([1, [2, 3], [4, [5, 6]]]) → [1, 2, 3, 4, 5, 6]
# Hints:
#   - Use isinstance(item, list) to check if an item is a list
#   - Base case: if the input list is empty, return []
#   - If the first item is a list: flatten it + flatten the rest
#   - If the first item is not a list: put it first + flatten the rest
# Write your code below:

