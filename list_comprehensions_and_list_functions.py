grid = [
    [0,0,0],
    [0,0,0]
]
num_row = 2
num_col = 3
item = [[0 for _ in range(num_col)] for _ in range(num_row)]
print(item)

lst = [1,2,-5,6]


result = []

# lambda arguments, create a lambda function to add 5 to a gice number
add_five = lambda x: x+5

answer = add_five(3)
print(f"\n{answer}")

# lambda with multiple arguments
# create a lambda function to multiply tow numbers
multiply = lambda x, y: x * y

# lambda with map()
# create a list with numbers
nums = [1,2,3]

# map a lambda function  to add 5 to each number in a list
mapped = map(lambda x: x+5, nums)

# convert map object to a list
outcome = list(mapped)
print(f"\n{outcome}")

# lambda with sorted()
# create a list of ruples with furits and prices
fruit_prices = [('banana', 3), ("apple", 1), ("orange", 5)]

# stort the list based on the prices of the fruit
sorted_prices = sorted(fruit_prices, key=lambda x: x[1])

print(f"\n{sorted_prices}")

