data = str(input())
new_str = ""
for char in data:
    if char.islower():
        new_str += char
    else:
        char = '_' + char.lower()
        new_str += char
print(new_str)
