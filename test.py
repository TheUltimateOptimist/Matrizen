class Test:
    def __init__(self, value):
        self.value = value

    def __plus__(self):
        self.value += 1

    def new(self, value):
        return Test(value)


print(Test(2).new(3).value)
