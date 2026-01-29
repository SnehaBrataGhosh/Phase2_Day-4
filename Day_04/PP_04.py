# 34. Sort a list without using built-in sort().
# Q34: Sort a list without using sort() (Selection Sort, Ultra-Deep)

def sort_list(nums):
    """
    Problem in simple words:
    We need to sort numbers from smallest to largest without using Python's sort().
    We'll use selection sort.
    """
    n = len(nums)
    print("Step 1: Original list:", nums)

    # Step 2: Loop through list to select the minimum each time
    for i in range(n):
        min_index = i
        print(f"\nIteration {i}: start min_index={min_index} (value={nums[min_index]})")
        for j in range(i+1, n):
            if nums[j] < nums[min_index]:
                print(f"  nums[{j}]={nums[j]} < nums[{min_index}]={nums[min_index]} -> update min_index")
                min_index = j
        # Swap
        print(f"  Swap nums[{i}]={nums[i]} with nums[{min_index}]={nums[min_index]}")
        nums[i], nums[min_index] = nums[min_index], nums[i]
        print(f"  List after swap: {nums}")

    print("\nFinal sorted list:", nums)
    return nums

# Example
sort_list([64, 25, 12, 22, 11])

"""
Dry Run:
- i=0: find min 11 at index 4 -> swap -> [11,25,12,22,64]
- i=1: find min 12 at index 2 -> swap -> [11,12,25,22,64]
- i=2: find min 22 at index 3 -> swap -> [11,12,22,25,64]
- i=3: min 25 at index 3 -> swap with itself
- i=4: min 64 -> swap with itself
Final sorted: [11,12,22,25,64]
"""
