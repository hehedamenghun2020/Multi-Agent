class Memory:
    def __init__(self):
        self.store = {}

    def add(self, key, value):
        if key not in self.store:
            self.store[key] = []
        self.store[key].append(value)

    def get_all(self):
        return self.store
