"""
You have a string:
sentence = "  apple, Banana, mango, APPLE, banana, Mango  "

Write code to:
1. Strip spaces
2. Split the string by commas
3. Convert all items to lowercase
4. Remove duplicates
5. Join them with a hyphen -
6. The final output should be sorted alphabetically
"""
sentence = "  apple, Banana, mango, APPLE, banana, Mango  "
items = sentence.strip().split(",")
cleaned = [i.strip().lower() for i in items]
unique = sorted(set(cleaned))
result = "-".join(unique)
print(result)


