from color import printRed


class Calculator:
    def __init__(self, a, b=0):
        self.a = a
        self.b = b

    def __matrixMatrix(self):
        if str(self.a.__class__) == "<class '__main__.Matrix'>" and self.a.__class__ == self.b.__class__:
            return True
        else:
            return False

    def __numberNumber(self):
        if str(self.a.__class__) == "<class 'number.Number'>" and self.a.__class__ == self.b.__class__:
            return True
        else:
            return False

    def __matrixNumber(self):
        if str(self.a.__class__) == "<class '__main__.Matrix'>" and str(self.b.__class__) == "<class '__main__.Number'>":
            return True
        else:
            return False

    def __numberMatrix(self):
        if str(self.a.__class__) == "<class '__main__.Number'>" and str(self.b.__class__) == "<class '__main__.Matrix'>":
            return True
        else:
            return False

    def __isMatrix(self):
        if str(self.a.__class__) == "<class '__main__.Matrix'>":
            return True
        else:
            return False

    def __isNumber(self):
        if str(self.a.__class__) == "<class '__main__.Number'>":
            return True
        else:
            return False

    def add(self):
        if self.__matrixMatrix():
            return self.a.addMatrix(self.b)
        elif self.__numberNumber():
            return self.a.addNumber(self.b)
        else:
            printRed(
                f"ERROR: DIE ADDITION DER KLASSEN {self.a.__class__} UND {self.b.__class__} IST NICHT DEFINIERT!")
            return None

    def subtract(self):
        if self.__matrixMatrix():
            return self.a.subtractMatrix(self.b)
        elif self.__numberNumber():
            return self.a.subtractNumber(self.b)
        else:
            printRed(
                f"ERROR: DIE SUBTRAKTION DER KLASSEN {self.a.__class__} UND {self.b.__class__} IST NICHT DEFINIERT!")
            return None

    def multiply(self):
        if self.__matrixMatrix():
            return self.a.multiplyWithMatrix(self.b)
        elif self.__numberNumber():
            return self.a.multiplyWithNumber(self.b)
        elif self.__numberMatrix():
            return self.a.multiplyWithNumber(self.b)
        elif self.__numberMatrix():
            return self.b.multiplyWithNumber(self.a)
        else:
            printRed(
                f"ERROR: DIE MULTIPLIKATION DER KLASSEN {self.a.__class__} UND {self.b.__class__} IST NICHT DEFINIERT!")
            return None

    def divide(self):
        if self.__matrixMatrix():
            return self.a.divideByMatrix(self.b)
        elif self.__numberNumber():
            return self.a.divideByNumber(self.b)
        elif self.__matrixNumber():
            return self.a.divideByNumber(self.b)
        else:
            printRed(
                f"ERROR: DIE DIVISION DER KLASSEN {self.a.__class__} UND {self.b.__class__} IST NICHT DEFINIERT!")
            return None

    def exponentiate(self):
        if self.__matrixNumber():
            return self.a.exponentiateByNumber(self.b)
        elif self.__numberNumber():
            return self.a.exponentiateByNumber(self.b)
        else:
            printRed(
                f"ERROR: DIE POTENZIERUNG DER KLASSEN {self.a.__class__} UND {self.b.__class__} IST NICHT DEFINIERT!")

    def squareRoot(self):
        if self.__isNumber():
            return self.a.takeSquareRoot()
        else:
            printRed(
                f"ERROR: DIE WURZEL DER KLASSE {self.a.__class__} IST NICHT DEFINIERT!")

    def transpose(self):
        if self.__isMatrix():
            return self.a.transpose()
        else:
            printRed(
                f"ERROR: DIE TRANSPONIERUNG DER KLASSE {self.a.__class__} IST NICHT DEFINIERT")
            return None

    def invert(self):
        if self.__isMatrix():
            return self.a.invert()
        else:
            printRed(
                f"ERROR: DIE INVERTIERUNG DER KLASSE {self.a.__class__} IST NICHT DEFINIERT")
