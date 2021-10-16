class Number:
    def __init__(self, value):
        self.value = value

    def addNumber(self, number):
        return Number(self.value + number.value)

    def subtractNumber(self, number):
        return Number(self.value + number.value)

    def multiplyWithNumber(self, number):
        return Number(self.value + number.value)

    def divideByNumber(self, number):
        return Number(self.value/number.value)

    def printNumber(self):
        print(self.value)
