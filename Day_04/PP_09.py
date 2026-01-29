# 39. Count frequency of each character in a string.
# Q39: Count frequency of each character in a string (Ultra-Deep)

def char_frequency(s):
    """
    Problem:
    Count how many times each character appears
    """
    freq = {}
    print("Step 1: Start with empty dict:", freq)

    for idx, char in enumerate(s):
        print(f"Checking char[{idx}]='{char}'")
        if char in freq:
            freq[char] += 1
            print(f"  Incremented freq[{char}]={freq[char]}")
        else:
            freq[char] = 1
            print(f"  Added freq[{char}]=1")

    print("\nFinal frequency:", freq)
    return freq

# Example
char_frequency("hello world")

"""
Dry Run:
- 'h' -> 1
- 'e' -> 1
- 'l' -> 1 -> 2 -> 3
- 'o' -> 1 -> 2
- ' ' -> 1
- 'w' ->1
- 'r' ->1
- 'd' ->1
Final: {'h':1,'e':1,'l':3,'o':2,' ':1,'w':1,'r':1,'d':1}
"""
