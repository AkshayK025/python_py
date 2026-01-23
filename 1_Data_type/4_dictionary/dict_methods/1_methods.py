my_dict = {}        #empty dictionary

# Dictionary of colors
f_colors = {"apple": "red", "banana": "yellow", "grape": "purple"}

print(f_colors.keys())  # Returns a view of the dictionary’s keys.

print()
print(f_colors.values()) #  Returns a view of the dictionary’s values.

print()
print(f_colors.items()) #  Returns a view of the dictionary’s key-value pairs.

print()
print(f_colors.get('apple')) #Returns the value for the specified key, or None if the key doesn’t exist
print(f_colors["banana"])

print()
f_colors.update({'apple':'dark red'})  #Updates the dictionary with supplied key-value pairs.


print()
print(f_colors.get('apple')) #Returns the value for the specified key, or None if the key doesn’t exist
f_colors["apple"] = 'red'
print(f_colors.get('apple'))