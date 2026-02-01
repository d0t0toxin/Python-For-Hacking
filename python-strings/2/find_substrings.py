"""
Find all substrings of a string
Goal: A substring is any continuous part of the string.
"""
string = "abcdef"
substrings = []
for start in range(len(string)):
    for end in range(start + 1, len(string) + 1):
        substrings.append(string[start:end])
print(substrings)


