"""
Remove all special characters from a string
Goal: Keep only letters and numbers; remove punctuation or symbols.
"""

import re
string = "hello@world!123"
cleaned_string = re.sub(r'[^A-Za-z0-9]', "", string)
print(cleaned_string)

sec_cleaned_string = "".join(x for x in string if x.isalnum())
print(sec_cleaned_string)

