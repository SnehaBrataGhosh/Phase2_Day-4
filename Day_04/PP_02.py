# 32. Find the largest and smallest element in a list.
# Q32: Find largest and smallest element in a list (Ultra-Deep Teaching Version)

def largest_smallest(nums):
    """
    Problem in simple words:
    We want to find the largest and smallest numbers in a given list.
    Largest = the number greater than all others.
    Smallest = the number smaller than all others.
    """

    # Step 1: Initialize largest and smallest
    largest = nums[0]   # assume first element is largest initially
    smallest = nums[0]  # assume first element is smallest initially
    print(f"Step 1: Start -> largest={largest}, smallest={smallest}")

    # Step 2: Loop through the list to compare each element
    for idx, n in enumerate(nums):
        print(f"\nChecking nums[{idx}]={n}")
        if n > largest:
            print(f"  {n} > largest({largest}) -> update largest")
            largest = n
            print(f"  New largest={largest}")
        if n < smallest:
            print(f"  {n} < smallest({smallest}) -> update smallest")
            smallest = n
            print(f"  New smallest={smallest}")

    # Step 3: Print final results
    print("\nFinal Output:")
    print("List:", nums)
    print("Largest:", largest)
    print("Smallest:", smallest)

# Example list
example_list = [12, 4, 56, 7, 89, 1]
largest_smallest(example_list)

"""
Step-by-Step Dry Run:

1. Start with largest=nums[0]=12, smallest=nums[0]=12
2. Loop through each element:
   - nums[0]=12 -> not greater than largest, not smaller than smallest -> skip
   - nums[1]=4 -> 4<smallest(12) -> smallest=4; 4>largest? no -> largest stays 12
   - nums[2]=56 -> 56>largest(12) -> largest=56; 56<smallest(4)? no -> smallest stays 4
   - nums[3]=7 -> 7>largest(56)? no; 7<smallest(4)? no -> skip
   - nums[4]=89 -> 89>largest(56) -> largest=89; 89<smallest(4)? no -> skip
   - nums[5]=1 -> 1<smallest(4) -> smallest=1; 1>largest(89)? no -> skip
3. Final largest=89, smallest=1
4. Print results
"""
