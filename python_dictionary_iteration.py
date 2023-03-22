# Example Dictionary

example = {
    'color': 'red',
    'fruit': 'apple',
    'species': 'dog',
}

# example key-value access
example['color']

# Use below to inspect your local environment
# Notice that this is a dictionary!
print(locals())

# unhashable type: 'list'
l = [1,2,3]
l[2] = 5
print(l)

# Example Dictionary

example = {
    'color': 'red',
    'fruit': 'apple',
    'species': 'dog',
}

# Basic iteration
for key in example:
    print(key)

# With values by accessing dict
for key in example:
    print(key, '->', example[key])

# Use the dir() function to examine Python objects
# dir({})

# .keys()
for key in example.keys():
    print(key)

# .values()
for value in example.values():
    print(value)

# .items()
for item in example.items():
    print(item)

# .items() with unpacking
for key, value in example.items():
    print(key, '->', value)
