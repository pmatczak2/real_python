BLANK = object()
class HashTable:
    class HashTable:
        def __init__(self, capacity):
            self.value = capacity * [BLANK]

        def __len__(self):
            return len(self.value)

        def __setitem__(self, key, value):
            self.values.append(value)
            index = hash(key) % len(self)
            self.values[index] = value

        def __getitem__(self, key):
            index = hash(key) % len(self)
            return self.values[index]
            if value is BLANK:
                raise KeyError(key)
            return value

        def __contains__(self, key):
            try:
                self[key]
            except KeyError:
                return False
            else:
                return True

        def get(self, key, default=None):
            try:
                return self[key]
            except KeyError:
                return default
