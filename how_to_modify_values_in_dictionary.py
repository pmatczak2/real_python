prices = {"apple": 0.5, "orange": 0.35, "bananna": 0.25}

for key in prices:
    prices[key] = prices[key] + .1
print(prices)

# Attempting to modify values with .items()
# Doesn't work!
# for key, value in prices.items():
#     value = value + .2


# Deleting key during iteration
# BAD IDEA
# prices['kiwi'] = 1
# for key in prices:
#     del prices['kiwi']

# Converting to a list avoids this problem
for key in list(prices.keys()):
    prices['kiwi'] = 2
print(prices)

# Modifying with key and dictionary access
# is the best policy!
prices['tomato'] = 0.2
print(prices)