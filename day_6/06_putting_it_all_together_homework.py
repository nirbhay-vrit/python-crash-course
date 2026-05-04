# ---------------------------------------------------------
# HOMEWORK 6: PUTTING IT ALL TOGETHER 🏗️
# Build your own mini-project using everything you've learned!
# ---------------------------------------------------------
#
# PROJECT: SHOPPING CART SYSTEM
# Build a simple shopping cart using functions.
#
# Required functions to write:
#
#   create_item(name, price, quantity=1, **extras)
#     → returns a dict with name, price, quantity, and any extras
#       e.g. create_item("Apple", 0.5, quantity=3, organic=True)
#
#   item_total(item)
#     → returns price * quantity for one item
#
#   apply_discount(price, percent=0)
#     → returns price after deducting the discount percentage
#
#   cart_subtotal(*items)
#     → returns the total of all item_total() values (use *args!)
#
#   add_tax(subtotal, tax_rate=0.1)
#     → returns subtotal + 10% tax
#
#   print_receipt(cart_name, *items, discount=0, tax_rate=0.1)
#     → prints a full receipt:
#       - header with cart name
#       - each item: name  qty x price  = total
#       - subtotal
#       - discount (if any)
#       - tax
#       - GRAND TOTAL
#
# Test your cart with at least 4 items.
# Apply a 10% discount and 8% tax.
#
# Example output (format is up to you, make it look nice!):
#
#   ==============================
#     MY SHOPPING CART
#   ==============================
#     Apple       3 x £0.50 = £1.50
#     Bread       1 x £1.20 = £1.20
#     Orange Juice 2 x £2.00 = £4.00
#     Chocolate   1 x £3.50 = £3.50
#   ------------------------------
#     Subtotal:        £10.20
#     Discount (10%):  -£1.02
#     Tax (8%):        £0.73
#   ==============================
#     TOTAL:           £9.91
#   ==============================
#
# Write your code below:




# ⭐ BONUS CHALLENGE:
# Add a 'compare_carts' function that takes two cart names and
# two lists of items, and prints which cart was cheaper and by how much.
# Write your code below:

