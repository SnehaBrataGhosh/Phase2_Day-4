# 38. Use list comprehension to generate squares of numbers 1–10.
# Q38: List comprehension for squares 1-10 (Ultra-Deep)

# Problem in simple words:
# We want squares of 1-10, i.e., 1^2,2^2,...10^2

squares = [x**2 for x in range(1,11)]
print("Squares 1-10:", squares)

"""
Dry Run:
- x=1 -> 1^2=1
- x=2 -> 4
- x=3 -> 9
...
- x=10 -> 100
Result: [1,4,9,16,25,36,49,64,81,100]
"""
