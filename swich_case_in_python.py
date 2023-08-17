"""
having a switch/case in python
if cond == 'cond_a':
    handle_a()
elif cond == 'cond_b':
    handle_b()
else:
    handle_default
Python are first class objects, which means you can pass them to other functions as arguments, return them from
other functions as values, and store them in variables and data structures. You’ll see how to assign a function to
a list data structure. This flexible feature in Python will allow you to emulate switch case.
def myfunc(a,b):
    return a + b

func = [myfunc]
funcs[0](2,3)

dictionary to map conditions to handler functions. Here’s a code snippet from the lesson that shows how to create a
dictionary mapping as well as how to call a function based on a condition:

func_dict = {
    'cond_a': handle_a
    'cond_b': handle_b
}
func_dict.get(cond, handle_default)()
"""

# Emulating Switch/Case in Python. In this lesson you’ll see a real world example of how you to emulate
# switch/case using a Python dictionary and lambda functions :

def dispatch_if(operator, x, y):
    if operator == 'add':
        return x + y
    elif operator == "sub":
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y
    return None
def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()

print(dispatch_dict('add',2,2))