# 43. Find the first non-repeated character in a string.
# Q43: First non-repeated character (Ultra-Deep)

def first_non_repeated(s):
    freq = {}
    print("Step 1: Build frequency dict")
    for char in s:
        freq[char] = freq.get(char,0)+1
        print(f"  {char}: {freq[char]}")

    print("Step 2: Find first non-repeated")
    for char in s:
        if freq[char]==1:
            print(f"First non-repeated: {char}")
            return char
    print("No unique character")
    return None

first_non_repeated("swiss")
 