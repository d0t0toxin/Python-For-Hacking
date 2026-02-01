"""
Reverse each word in a sentence
"""
string = "External things are not the problem. It’s your judgment of them. And you can erase that right now."
# print(string[::-1]) --> this reverse the whole the string btw
reversed_string = " ".join(word[::-1] for word in string.split())
print(reversed_string)



