from mathFunctionality import getNumbersLengthList
from matrixCalculator import MatrixCalculator


class Matrix:
    def __init__(self, name):
        self.value = []
        self.name = name

    def getDimensions(self):
        if len(self.value) == 0:
            return [0, 0]
        else:
            return [len(self.value), len(self.value[0])]

    def getMatrixSum(self):
        sum = 0
        for list in self.value:
            for element in list:
                sum += element
        return sum

    def printMatrix(self):
        list = self.value
        print(list)
        additionalSpaces = getNumbersLengthList(list)
        for i, row in enumerate(list):
            outputString = ""
            for j, element in enumerate(row):
                outputString += str(element)
                outputString += additionalSpaces[i][j]*" "
            print(outputString)

    def isQuadraticMatrix(self):
        if len(self.value) == len(self.value[0]):
            return True
        else:
            return False

    def isUpperTriangleMatrix(self):
        m = len(self.value)
        if self.isQuadraticMatrix():
            result = True
            for i in range(m):
                for j in range(m):
                    if j < i and self.value[i][j] != 0:
                        result = False
            return result
        else:
            return False

    def isLowerTriangleMatrix(self):
        m = len(self.value)
        if self.isQuadraticMatrix():
            result = True
            for i in range(m):
                for j in range(m):
                    if i < j and self.value[i][j] != 0:
                        result = False
            return result
        else:
            return False

    def isIdentityMatrix(self):
        m = len(self.value)
        if self.isQuadraticMatrix():
            result = True
            for i in range(m):
                for j in range(m):
                    if (i == j and self.value[i][j] != 1) or (i != j and self.value[i][j] != 0):
                        result = False
            return result
        else:
            return False

    def isNullMatrix(self):
        m = len(self.value)
        n = len(self.value[0])
        for i in range(m):
            for j in range(n):
                if self.value[i][j] != 0:
                    return False
        return True

    def isDiagonalMatrix(self):
        m = len(self.value)
        if self.isQuadraticMatrix():
            for i in range(m):
                for j in range(m):
                    if i != j and self.value[i][j] != 0:
                        return False
            return True
        else:
            return False

    def isSymmetricMatrix(self):
        if self.isQuadraticMatrix():
            m = len(self.value)
            transponedMatrix = MatrixCalculator.transpose(self.value)
            for i in range(m):
                for j in range(m):
                    if self.value[i][j] != transponedMatrix[i][j]:
                        return False
            return True
        else:
            return False

    def getProperties(self):
        properties = []
        if self.isNullMatrix():
            properties.append("Nullmatrix")
        if self.isQuadraticMatrix():
            properties.append("quadratische Matrix")
            if self.isSymmetricMatrix():
                properties.append("symmetrische Matrix")
            if self.isIdentityMatrix():
                properties.append("Einheitsmatrix")
                properties.append("Diagonalmatrix")
                properties.append("obere Dreieckmatrix")
                properties.append("untere Dreiecksmatrix")
            elif self.isDiagonalMatrix():
                properties.append("Diagonalmatrix")
                properties.append("obere Dreiecksmatrix")
                properties.append("untere Dreiecksmatrix")
            elif self.isUpperTriangleMatrix():
                properties.append("obere Dreiecksmatrix")
            elif self.isLowerTriangleMatrix():
                properties.append("untere Dreiecksmatrix")
        return properties

    def isInvertable(self):
        # todo: implement invertable checking
        # following return statement is only for now
        return False
