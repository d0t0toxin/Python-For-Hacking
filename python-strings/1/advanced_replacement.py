"""
Given:
data = "Error-404, Error-500, Error-404, Error-403"

Do the following in as few lines as possible:
1. Replace all "Error" with "Warning"
2. Split the string into individual codes (e.g., "Warning-404")
3. Count how many "Warning-404" codes exist
4. Join them back into a single string separated by "; "
"""

data = "Error-404, Error-500, Error-404, Error-403"
# replacing Error with Warning
replaced_data = data.replace("Error", "Warning")
# spliting the string
clean_data = replaced_data.split(",")
more_clean_data = [i.strip() for i in clean_data] # removing whitespaces to clean the string
# the count to the given string in the array
print(more_clean_data.count("Warning-404"))
# the last and final
single_string = "; ".join(more_clean_data)
print(single_string)



