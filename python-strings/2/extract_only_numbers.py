"""
Extract only numbers from a string
Goal: Remove all letters/special characters and keep only the numbers.
"""
string = "ab12cd34"
only_nums = [x for x in string if x.isdigit()]
print("".join(only_nums))

