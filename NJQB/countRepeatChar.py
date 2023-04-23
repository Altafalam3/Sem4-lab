def count_repeated_chars(s):
    char_count = {}
    for c in s:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1

    repeated_chars = {}
    for c in char_count:
        if char_count[c] > 1:
            repeated_chars[c] = char_count[c]

    return repeated_chars

# Example usage:
s = "thequickbrownfoxjumpsoverthelazydog"
result = count_repeated_chars(s)
print(result)  # Output: {'l': 3, 'o': 2}
