from mathFunctions import isNumber, getClosingBraceIndex
from number import Number
from variables import Variables
from matrixGenerator import MatrixGenerator


class TokenListPreparer:
    def __init__(self, tokenList):
        self.tokenList = tokenList

    def __mergeDoubleOperators(self):
        i = 0
        while i < len(self.tokenList):
            if (self.tokenList[i] == "+" and self.tokenList[i - 1] == "+") or (self.tokenList[i] == "-" and self.tokenList[i - 1] == "-"):
                self.tokenList[i - 1] = "+"
                del self.tokenList[i]
                # i wird nicht erhöht
            elif (self.tokenList[i] == "-" and self.tokenList[i - 1] == "+") or (self.tokenList[i] == "+" and self.tokenList[i - 1] == "-"):
                self.tokenList[i - 1] = "-"
                del self.tokenList[i]
                # i wird nicht erhöht
            else:
                # i wird um eins erhöht
                i += 1
        i = 0
        while i < len(self.tokenList):
            # delete all "+" whose left neighbour is an "*", "/", "^"
            if (self.tokenList[i] == "*" and self.tokenList[i + 1] == "+") or (self.tokenList[i] == "^" and self.tokenList[i + 1] == "+") or (self.tokenList[i] == "/" and self.tokenList[i + 1] == "+"):
                del self.tokenList[i + 1]
                i += 1
            # if suquence "*" -> "-" or "(" -> "-" is found: convert - to "-1", "*"
            elif (self.tokenList[i] == "*" and self.tokenList[i + 1] == "-") or (self.tokenList[i] == "(" and self.tokenList[i + 1] == "-"):
                self.tokenList[i + 1] = "-1"
                self.tokenList.insert(i + 2, "*")
                i += 2
            # if sequence ^- or /- occurs: convert to ^(-1*...) or /(-1*...)
            elif (self.tokenList[i] == "^" and self.tokenList[i + 1] == "-") or (self.tokenList[i] == "/" and self.tokenList[i + 1] == "-"):
                if self.tokenList[i + 2] == "(":
                    self.tokenList.insert(
                        getClosingBraceIndex(i + 2, self.tokenList) + 1)
                else:
                    self.tokenList.insert(i + 3, ")")
                self.tokenList[i + 1] = "-1"
                self.tokenList.insert(i + 2, "*")
                self.tokenList.insert(i + 1, "(")
                i = getClosingBraceIndex(i + 1, self.tokenList) + 1
            else:
                i += 1

    def __convertNumbers(self):
        for i, token in enumerate(self.tokenList):
            if isNumber(token):
                self.tokenList[i] = Number(float(self.tokenList[i]))

    def __dissolveVariables(self):
        for i, token in enumerate(self.tokenList):
            if Variables().contains(token):
                self.tokenList[i] = Variables().getValue(token)

    def __dissolveGenerators(self):
        for i, token in enumerate(self.tokenList):
            dissolved = MatrixGenerator().generateMatrix(token)
            if dissolved != None:
                self.tokenList[i] = dissolved

    def prepare(self):
        if self.tokenList[0] == "-" or self.tokenList[0] == "+":
            self.tokenList.insert(0, "0")
        self.__mergeDoubleOperators()
        self.__convertNumbers()
        self.__dissolveVariables()
        self.__dissolveGenerators()
        return self.tokenList
