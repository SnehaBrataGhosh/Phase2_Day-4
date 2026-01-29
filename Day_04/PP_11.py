# 41. Check if a string is palindrome.
# Q41: Check palindrome (Ultra-Deep)

def is_palindrome(s):
    """
    Problem: Check if string reads same forwards and backwards
    """
    s_clean = s.lower().replace(" ","")  # normalize
    print("Normalized string:", s_clean)
    rev = s_clean[::-1]
    print("Reversed string:", rev)

    if s_clean == rev:
        print("Result: Palindrome ✅")
        return True
    else:
        print("Result: Not Palindrome ❌")
        return False

# Example
is_palindrome("Race car")

"""
Dry Run:
- Normalize: "racecar"
- Reverse: "racecar"
- Compare: equal -> palindrome
"""
