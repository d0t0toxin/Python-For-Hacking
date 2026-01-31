"""
Find the most frequent character in the string
"""

marcus_text = "Everything we hear is an opinion, not a fact. Everything we see is a perspective, not the truth."
frequency = {}

for char in marcus_text:
    if char in frequency:
        frequency[char] += 1
    else:
       frequency[char] = 1

most_frequent = None
max_count = 0
for char, count in frequency.items():
    if count > max_count:
        max_count = count
        most_frequent = char
print(f"{most_frequent}: {max_count}")

