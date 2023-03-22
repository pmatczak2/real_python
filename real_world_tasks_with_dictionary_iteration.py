# Example
a_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
}

# Swapping keys and values
new_dict = {}
for key, value in a_dict.items():
    new_dict[value] = key
print(new_dict)

# Filtering contents of a dictionary
new_dict = {}
for key, value in a_dict.items():
    if value > 2:
        new_dict[key] = value
print(new_dict)

# New demonstration dictionary
incomes = {
    'jeff': 12000,
    'annie': 23000,
    'glen': 50000,
}
# Summing values
total_income = 0
for key, income in incomes.items():
    total_income += income
print(total_income)

