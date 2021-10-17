class Variables:
    def __init__(self):
        self.names = []
        self.values = []

    def add(self, name, value):
        self.names.append(name)
        self.values.append(value)

    def remove(self, name):
        for i, variable in enumerate(self.names):
            if variable == name:
                del self.names[i]
                del self.values[i]
                break

    def contains(self, name):
        for variable in self.names:
            if variable == name:
                return True
        return False

    def getValue(self, name):
        for i, variable in enumerate(self.names):
            if variable == name:
                return self.values[i]
        return None
