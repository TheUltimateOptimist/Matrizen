from listHelper import split_list, delete_range
from calculator import Calculator
from tokenListPreparer import TokenListPreparer
from tokenizer import Tokenizer
from mathFunctions import getClosingBraceIndex


class Term:
    def __init__(self, textString):
        self.tokensList = TokenListPreparer(
            Tokenizer().tokenize(textString)).prepare()

    def __printSolution(self, solution):
        if str(solution.__class__) == "<class 'matrix.Matrix'>":
            solution.printMatrix()
        elif str(solution.__class__) == "<class 'number.Number'>":
            solution.printNumber()

    def calculate(self, shouldPrint=False):
        i = 0
        while i < len(self.tokensList):
            token = self.tokensList[i]
            if token == "(":
                print(i)
                print(self.tokensList)
                closingBraceIndex = getClosingBraceIndex(
                    i, self.tokensList)
                print("kdddk:")
                print(closingBraceIndex)
                self.tokensList[i] = self.calculate(split_list(
                    i + 1, closingBraceIndex - 1, self.tokensList))
                self.tokensList = delete_range(
                    i + 1, closingBraceIndex, self.tokensList)
            i += 1
        i = 0
        while i < len(self.tokensList):
            token = self.tokensList[i]
            if token.__class__ == "<class 'str'>" and token == "*":
                self.tokensList[i] = Calculator(
                    self.tokensList[i - 1], self.tokensList[i + 1]).multiply()
                del self.tokensList[i + 1]
                del self.tokensList[i - 1]
            elif token.__class__ == "<class 'str'>" and token == "/":
                self.tokensList[i] = Calculator(
                    self.tokensList[i - 1], self.tokensList[i + 1]).divide()
                del self.tokensList[i + 1]
                del self.tokensList[i - 1]
            elif token.__class__ == "<class 'str'>" and token == "^":
                self.tokensList[i] = Calculator(
                    self.tokensList[i + -1], self.tokensList[i - 1]).exponentiate()
                del self.tokensList[i + 1]
                del self.tokensList[i - 1]
            elif token.__class__ == "<class 'str'>" and token == "transp":
                self.tokensList[i] = Calculator(
                    self.tokensList[i + 1]).transpose()
                del self.tokensList[i + 1]
                i += 1
            elif token.__class__ == "<class 'str'>" and token == "invert":
                self.tokensList[i] = Calculator(
                    self.tokensList[i + 1]).invert()
                del self.tokensList[i + 1]
                i += 1
            else:
                i += 1
        i = 0
        while i < len(self.tokensList):
            token = self.tokensList[i]
            if token == "+":
                print(f"+: {i}")
                self.tokensList[i] = Calculator(
                    self.tokensList[i - 1], self.tokensList[i + 1]).add()
                del self.tokensList[i + 1]
                del self.tokensList[i - 1]
            elif token == "-":
                print(f"-: {i}")
                self.tokensList[i] = Calculator(
                    self.tokensList[i - 1], self.tokensList[i + 1]).subtract()
                del self.tokensList[i + 1]
                del self.tokensList[i - 1]
            else:
                i += 1
        print(self.tokensList)
        if shouldPrint:
            self.__printSolution(self.tokensList[0])
        return self.tokensList[0]
