"""
Check whether the string is palindrome or not
Word: level, radar, madam
Number: 121, 1331
"""
phrase = "A man, a plan, a canal, Panama"
clean_str = phrase.replace(" ", "").replace(",", "").lower()
if clean_str == clean_str[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
###
word = "level"
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


