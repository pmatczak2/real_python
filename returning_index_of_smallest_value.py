numbers = [1, 5, 88, 6, 7, 33, 4, 99, 9999, -58, -66, 48, 77]

# return the value and the index of the smallest number of the list

def find_smallest_value(values):
    return sorted(values)[0]



def find_position(values, item):
    return values.index(item)

assert find_smallest_value(numbers) == -66

assert find_position(numbers, 88) == 2

assert find_position(numbers, find_smallest_value(numbers)) == 10