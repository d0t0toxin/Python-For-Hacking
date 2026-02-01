"""
Validate a password string:
min 8 chars
at least 1 digit
at least 1 uppercase
"""
user_input = input("Enter a valid password: ")
if (
        len(user_input) >= 8
        and any(char.isdigit() for char in user_input)
        and any(char.isupper() for char in user_input)
):
    print("Password is valid")
else:
    print("Password is not valid")

# By using regular expressions
import re
pattern = r'^(?=.*[A-Z])(?=.*\d).{8,}$'

if re.match(pattern, user_input):
    print("It is a valid password.")
else:
    print("It is not a valid password.")

