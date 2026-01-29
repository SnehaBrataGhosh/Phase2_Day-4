# 42. Check if two strings are anagrams.
# Q42: Check anagrams (Ultra-Deep)

def are_anagrams(s1,s2):
    """
    Problem: Two strings are anagrams if same letters in different order
    """
    s1_clean = s1.replace(" ","").lower()
    s2_clean = s2.replace(" ","").lower()
    print(f"Normalized: s1='{s1_clean}', s2='{s2_clean}'")

    sorted_s1 = sorted(s1_clean)
    sorted_s2 = sorted(s2_clean)
    print(f"Sorted: {sorted_s1}, {sorted_s2}")

    if sorted_s1 == sorted_s2:
        print("Result: Anagrams ✅")
        return True
    else:
        print("Result: Not Anagrams ❌")
        return False

# Example
are_anagrams("listen","silent")
                                             