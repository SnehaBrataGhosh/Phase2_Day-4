# 37. Flatten a nested list [[1,2],[3,4],[5]] into [1,2,3,4,5].
# Q37: Flatten a nested list (Ultra-Deep)

def flatten_list(nested):
    """
    Problem in simple words:
    Convert [[1,2],[3,4],[5]] -> [1,2,3,4,5] by extracting all elements
    """
    flat = []
    print("Step 1: Start with empty list:", flat)

    for i, sublist in enumerate(nested):
        print(f"\nChecking sublist[{i}]={sublist}")
        for j, item in enumerate(sublist):
            print(f"  Append sublist[{i}][{j}]={item} to flat")
            flat.append(item)
            print(f"  Flat now: {flat}")

    print("\nFinal flattened list:", flat)
    return flat

# Example
flatten_list([[1,2],[3,4],[5]])

"""
Dry Run:
- Start: flat=[]
- sublist[0]=[1,2] -> append 1,2 -> flat=[1,2]
- sublist[1]=[3,4] -> append 3,4 -> flat=[1,2,3,4]
- sublist[2]=[5] -> append 5 -> flat=[1,2,3,4,5]
Final: [1,2,3,4,5]
"""
