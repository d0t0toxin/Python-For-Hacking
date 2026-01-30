"""
You have:
msg = "Find the needle in the haystack. Needle is tricky."

Task:
1. Convert the string to lowercase
2. Count how many times "needle" occurs
3. Find the index of the first "needle"
4. Check if the string starts with "find" and ends with "tricky."
"""
msg = "Find the needle in the haystack. Needle is tricky."
# string to lowercase
lower_str = msg.lower()

# count occurence to "niddle"
niddle_count = lower_str.count("needle")

# returns the index of the first occurence
index_str = lower_str.find("needle")

# printing everything
print(lower_str)
print(index_str)
print(niddle_count)

if lower_str.startswith("find") and lower_str.endswith("tricky."):
    print("Everything is good")
else:
    print("Everything is not good")




