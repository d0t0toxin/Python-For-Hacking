"""
Given:
raw = "   Hello! Hello!! HELLO!!! hElLo?   "

Write a Python code snippet to:
1. Strip spaces
2. Convert everything to lowercase
3. Replace all punctuation (!, ?) with nothing
4. Split the string into words
5. Count how many times "hello" occurs
"""
raw = "   Hello! Hello!! HELLO!!! hElLo?   "
clean_str = raw.strip().lower()
print(clean_str)
#replacing punctuation
rep_str = clean_str.replace("!","").replace("?", "")
print(rep_str)
# spliting into words
splited_str = rep_str.split(" ")
print(splited_str)
# counting the hello
print(splited_str.count("hello"))

