def firstUniqChar(s):
    char_freq = {}

    # Update character frequencies
    for char in s:
        char_freq[char] = char_freq.get(char, 0) + 1

    # Find first non-repeating character
    for i, char in enumerate(s):
        if char_freq[char] == 1:
            return i

    return -1  # Add solution for First Unique Character in a String
# Example usage:
s = "leetcode"
print(firstUniqChar(s))  # Output: 0

s = "loveleetcode"
print(firstUniqChar(s))  # Output: 2

s = "aabbcc"
print(firstUniqChar(s))  # Output: -1 (no non-repeating character)
