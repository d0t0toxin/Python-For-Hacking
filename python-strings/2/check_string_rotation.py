"""
Check if one string is a rotation of another
Goal: One string is a rotation of another if you can shift it around to get the other string.
"""
s1 = "abcd"
s2 = "cdab"

if s2 in (s1+s1):
    print("yes s2 is the rotation of s1")
else:
    print("No s2 is not the rotation of s1")

