"""
Longest Substring Without Repeating Characters
Problem:
Given a string s, find the length of the longest substring without repeating characters.
Example:
s = "abcabcbb" → 3 ("abc")
Hint: Sliding window + hash map.
"""
s = "abcabcbb" 
def longest_unique_substring(s):
    last_seen = {}
    left = 0
    max_len = 0

    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        max_len = max(max_len, right - left + 1)

    return max_len
print(longest_unique_substring(s))
