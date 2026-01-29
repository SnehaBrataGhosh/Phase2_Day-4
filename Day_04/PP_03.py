# 33. Remove duplicates from a list.
# Q33: Remove duplicates from a list (Ultra-Deep Teaching Version)

def remove_duplicates(nums):
    """
    Problem in simple words:
    We want to remove repeated numbers from a list while keeping original order.
    """
    unique = []  # empty list to store unique numbers
    print("Step 1: Start with empty unique list:", unique)

    # Step 2: Loop through each number in original list
    for idx, n in enumerate(nums):
        print(f"\nChecking nums[{idx}]={n}")
        if n not in unique:
            print(f"  {n} not in unique -> add it")
            unique.append(n)
            print(f"  Updated unique list: {unique}")
        else:
            print(f"  {n} already in unique -> skip it")

    print("\nFinal unique list:", unique)
    return unique

# Example list
example_list = [1, 2, 2, 3, 4, 4, 5, 1]
remove_duplicates(example_list)

"""
Dry Run:
- Start: unique=[]
- nums[0]=1 -> not in unique -> add -> unique=[1]
- nums[1]=2 -> not in unique -> add -> unique=[1,2]
- nums[2]=2 -> already in unique -> skip
- nums[3]=3 -> add -> unique=[1,2,3]
- nums[4]=4 -> add -> unique=[1,2,3,4]
- nums[5]=4 -> skip
- nums[6]=5 -> add -> unique=[1,2,3,4,5]
- nums[7]=1 -> skip
Final unique list: [1,2,3,4,5]
"""
