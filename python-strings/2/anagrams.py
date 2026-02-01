"""
Check if two strings are anagrams
Goal: Two strings are anagrams if they have the same characters with the same frequency but possibly in a different order.
"""

str1 = "Listen"
str2 = "Silent"
clean_str1 = str1.strip().lower()
clean_str2 = str2.strip().lower()

if len(clean_str1) != len(clean_str2):
    print("Not Anagram")
else:
    for char in clean_str2:
        if char in clean_str1:
            clean_str1 = clean_str1.replace(char, "", 1)
        else:
            print("Not Anagram")
            break
    else:
        print("Anagrams")

clean_str1 = str2.lower().strip()
