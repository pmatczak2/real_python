animals = ["cat", "dog", "cheetah"]

print(sorted(animals))

animals = [
    {"type": "dog", "name": "love", "age": 8},
    {"type": "cat", "name": "vera", "age": 10},
    {"type": "bigcat", "name": "lauren", "age": 5}
    ]

print(sorted(animals, key=lambda animal: animal['age']))

animals.sort(key=lambda animal: animal['age'])
print(animals)



