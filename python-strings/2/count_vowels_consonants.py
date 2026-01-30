"""
Count vowels and consonants in a string.
"""
_string = "Hello World!"
vowels = "aeiouAEIOU"
vow_count = 0
conso_count = 0
for char in _string:
    if char.isalpha():
        if char in vowels:
            vow_count += 1
        else:
            conso_count += 1
print(vow_count)
print(conso_count)

