# 44. Reverse each word in a sentence: "hello world" → "olleh dlrow".
# Q44: Reverse each word in a sentence (Ultra-Deep)

def reverse_words(sentence):
    words = sentence.split()
    print("Words split:", words)
    reversed_words = [w[::-1] for w in words]
    print("Reversed each word:", reversed_words)
    result = " ".join(reversed_words)
    print("Final sentence:", result)
    return result

reverse_words("hello world")
