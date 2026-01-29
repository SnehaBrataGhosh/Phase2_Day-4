# 36. Find second largest number in a list.
# Q36: Second largest number in a list (Deep Trace Version)
def second_largest(nums):
    # Initialize largest and second largest to very small numbers
    largest = float("-inf")
    second = float("-inf")
    print("Initial: largest =", largest, ", second =", second)
    
    for idx, n in enumerate(nums):
        print("\nChecking nums[{}]={}".format(idx, n))
        if n > largest:
            print("  {} > largest({})".format(n, largest))
            second = largest   # previous largest becomes second largest
            largest = n        # update largest
            print("  Updated: largest =", largest, ", second =", second)
        elif n > second and n != largest:
            print("  {} > second({}) and != largest({})".format(n, second, largest))
            second = n         # update second largest
            print("  Updated second =", second)
        else:
            print("  {} is not larger than largest({}) or second({})".format(n, largest, second))
    
    return second

# Example list
example_list = [10, 20, 4, 45, 99, 99]
print("\nExample list:", example_list)
result = second_largest(example_list)
print("\n36) Second largest is:", result)

"""
Step-by-step explanation:

1. Start with largest = -inf, second = -inf
2. Iterate through the list:
   - 10: 10 > -inf -> largest=10, second=-inf
   - 20: 20 > 10 -> largest=20, second=10
   - 4: 4 not > largest(20), 4 > second(10)? no -> ignore
   - 45: 45 > 20 -> largest=45, second=20
   - 99: 99 > 45 -> largest=99, second=45
   - 99: 99 not > largest(99), 99 > second(45)? yes but 99==largest -> skip
3. Final second largest = 45
"""
