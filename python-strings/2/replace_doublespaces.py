"""
Replace multiple spaces with a single space
Goal: If a sentence has extra spaces, reduce them to only one.
"""
string = "This  is the          given string      for the         question!!!"
print(" ".join(string.split()))





