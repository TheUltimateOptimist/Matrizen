from littleFunctions.color import printRed
from littleFunctions.listHelper import getNumbersLengthList
from MatricesAndNumbers.number import Number


class Matrix:
    def __init__(self, value):
        self.value = value

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
        return Number(sum)

    def printMatrix(self):
        list = self.value
        additionalSpaces = getNumbersLengthList(list)
        for i, row in enumerate(list):
            outputString = ""
            for j, element in enumerate(row):
                outputString += str(element)
                outputString += additionalSpaces[i][j]*" "
            print(outputString)
        return True

    def addMatrix(self, matrix):
        if (len(self.value) == len(matrix.value)) and (len(self.value[0]) == len(matrix.value[0])):
            newValue = []
            for i, row in enumerate(self.value):
                newRow = []
                for j, number in enumerate(row):
                    newRow.append(number + matrix.value[i][j])
                newValue.append(newRow)
            return Matrix(newValue)
        else:
            print(
                "ERROR: FÜR DIE ADDITION ZWEIER MATRIZEN MÜSSEN DIE DIMENSIONEN ÜBEREINSTIMMEN")
            return None

    def subtractMatrix(self, matrix):
        if (len(self.value) == len(matrix.value)) and (len(self.value[0]) == len(matrix.value[0])):
            newValue = []
            for i, row in enumerate(self.value):
                newRow = []
                for j, number in enumerate(row):
                    newRow.append(number - matrix.value[i][j])
                newValue.append(newRow)
            return Matrix(newValue)
        else:
            print(
                "ERROR: FÜR DIE SUBTRAKTION ZWEIER MATRIZEN MÜSSEN DIE DIMENSIONEN ÜBEREINSTIMMEN")
            return None

    def multiplyWithMatrix(self, matrix):
        # Zwei Matrizen lassen sich nur dann miteinander multiplizieren,
        # wenn die Spaltenanzahl der ersten Matrix mit der Zeilenanzahl
        # der zweiten Matrix übereinstimmt.
        return matrix

    def divideByMatrix(self, matrix):
        # todo: implement matrix division
        # following return statement is just for now
        return matrix

    def exponentiateByNumber(self, number):
        # todo: implement matrix division
        # following return statement is just for now
        return self

    def divideByNumber(self, number):
        if not self.value:
            return self
        if number.value == 0:
            printRed("ERROR: DAS TEILEN DURCH O IST NICHT DEFINIERT!")
        else:
            return self.multiplyWithNumber(Number(1/number.value))

    def multiplyWithNumber(self, number):
        newValue = []
        for row in self.value:
            newRow = []
            for element in row:
                newRow.append(number.value*element)
            newValue.append(newRow)
        return Matrix(newValue)

    def transpose(self):
        # Zeilen der Eingansmatrix werden zu Spalten der Ausgangsmatrix
        # return self again if self is a matrix without any entrys
        if not self.value:
            return self
        newValue = []
        for i in range(len(self.value[0])):
            newRow = []
            for row in self.value:
                newRow.append(row[i])
            newValue.append(newRow)
        return Matrix(newValue)

    def invert(self):
        # todo: implement matrix inversing
        # following return statement is just for now
        return 0

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
            transponedMatrix = Matrix(self.value).transpose()
            for i in range(m):
                for j in range(m):
                    if self.value[i][j] != transponedMatrix.value[i][j]:
                        return False
            return True
        else:
            return False

    def isInvertableMatrix(self):
        # todo implement invertable checking
        # following returrn statement is just for now
        return False

    def getAttributes(self):
        properties = []
        if self.isNullMatrix():
            properties.append("Nullmatrix")
        if self.isQuadraticMatrix():
            properties.append("quadratisch")
            if self.isSymmetricMatrix():
                properties.append("symmetrisch")
            if self.isInvertableMatrix():
                properties.append("invertierbar")
            if self.isIdentityMatrix():
                properties.append("Einheitsmatrix")
                properties.append("Diagonalmatrix")
                properties.append("obere Dreiecksmatrix")
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
