# 40. Remove all vowels from a string.
# Q40: Remove all vowels (Ultra-Deep)

def remove_vowels(s):
    vowels = set("aeiouAEIOU")
    result = ""
    print("Step 1: Remove vowels from string:", s)

    for idx, char in enumerate(s):
        if char not in vowels:
            result += char
            print(f"  Keep '{char}' -> result='{result}'")
        else:
            print(f"  Remove vowel '{char}'")

    print("\nFinal result:", result)
    return result

# Example
remove_vowels("Hello World")

"""
Dry Run:
- 'H' -> keep
- 'e' -> remove
- 'l' -> keep
- 'l' -> keep
- 'o' -> remove
- ' ' -> keep
- 'W' -> keep
- 'o' -> remove
- 'r' -> keep
- 'l' -> keep
- 'd' -> keep
Final: "Hll Wrld"
"""
        