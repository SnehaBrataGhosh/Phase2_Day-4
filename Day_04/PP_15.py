# 45. Find longest word in a sentence.
# Q45: Find longest word in sentence (Ultra-Deep)

def longest_word(sentence):
    words = sentence.split()
    longest = words[0]
    print("Step 1: Words split:", words)
    for w in words:
        print(f"Checking word '{w}' length={len(w)} vs longest '{longest}' length={len(longest)}")
        if len(w) > len(longest):
            longest = w
            print(f"  Update longest='{longest}'")
    print("Final longest word:", longest)
    return longest

longest_word("I love programming in Python")
