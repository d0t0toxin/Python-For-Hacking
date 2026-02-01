"""
Convert a string from snake_case to camelCase
Goal: Convert strings like my_variable_name → myVariableName
"""
string = "my_variable_name"
camel_case = string.split("_")[0] + "".join(x.title() for x in string.split("_")[1:])
print(camel_case)



