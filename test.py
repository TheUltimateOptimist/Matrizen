class Test:
    def __init__(self, value):
        self.value = value

    def __plus__(self):
        self.value += 1


test = Test(3)
print(test.value)
