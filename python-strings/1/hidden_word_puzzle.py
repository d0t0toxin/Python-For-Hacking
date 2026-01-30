"""
You are given the string:
text = "  PyThOn Is Fun! Let's Learn Python.  "

Write a single line of Python code to:
1. Remove leading and trailing spaces
2. Convert all letters to lowercase
3. Replace "python" with "Java"
4. Count how many times "java" appears in the final string
"""

text = "  PyThOn Is Fun! Let's Learn Python.  "
print(text.strip().lower().replace("python", "java").count("java")) 


