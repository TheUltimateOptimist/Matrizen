class Test:
    def __init__(self, value):
        self.value = value

    def __plus__(self):
        self.value += 1

    def new(self, value):
        return Test(value)


print(Test(2).__class__)

i = 0
list = [1, 2, 3, 4, 5, 6, 7, 8]
while i < len(list):
    list.pop()
    print(list[i])
    i += 1
