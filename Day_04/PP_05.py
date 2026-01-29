# 35. Reverse a list without using reverse().
# Q35: Reverse a list without using reverse() (Ultra-Deep)

def reverse_list(nums):
    """
    Problem in simple words:
    Reverse the list by swapping first with last, second with second last, etc.
    """
    left = 0
    right = len(nums) - 1
    print("Step 1: Original list:", nums)

    while left < right:
        print(f"  Swap nums[{left}]={nums[left]} with nums[{right}]={nums[right]}")
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
        print(f"  List now: {nums}")

    print("\nFinal reversed list:", nums)
    return nums

# Example
reverse_list([1,2,3,4,5])

"""
Dry Run:
- Swap nums[0]=1 with nums[4]=5 -> [5,2,3,4,1]
- Swap nums[1]=2 with nums[3]=4 -> [5,4,3,2,1]
- left=2, right=2 -> stop
Final: [5,4,3,2,1]
"""
