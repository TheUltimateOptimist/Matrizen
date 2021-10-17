from color import printRed


class Number:
    def __init__(self, value):
        self.value = value

    def addNumber(self, number):
        return Number(self.value + number.value)

    def subtractNumber(self, number):
        return Number(self.value - number.value)

    def multiplyWithNumber(self, number):
        return Number(self.value + number.value)

    def divideByNumber(self, number):
        if number.value == 0:
            printRed("ERROR: DAS TEILEN DURCH O IST NICHT DEFINIERT!")
            return None
        else:
            return Number(self.value/number.value)

    def printNumber(self):
        print(self.value)

    def exponentiateByNumber(self, number):
        return Number(self.value**number.value)

    def takeSquareRoot(self):
        if self.value <= 0:
            printRed("ERROR: DIE WURZEL EINER NEGATIVEN ZAHL IST NICHT DEFINIERT!")
            return None
        else:
            import math
            return Number(math.sqrt(self.value))
