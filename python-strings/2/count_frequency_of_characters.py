"""
Count the frequency of each character in a string
"""

some_word = "Do not act as if you were going to live ten thousand years."
frequency ={}

for char in some_word:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
for i, j in frequency.items():
    print(f"{i}: {j}")

