import random

allMatrices = []
matrixArten = ["Benutzereingabe", "symmetrischeMatrix", "obereDreiecksmatrix",
               "untereDreiecksmatrix", "Einheitsmatrix", "Nullmatrix", "Diagonalmatrix", "quadratischeMatrix"]


def removeMatrix(name):
    for element in allMatrices:
        if element.name == name:
            allMatrices.remove(element)
            break


def getMatrix(name):
    for element in allMatrices:
        if element.name == name:
            return element
    return None


def getNumbersLengthList(list):
    lengthList = []
    maxLengths = []
    for i, row in enumerate(list):
        for j, element in enumerate(row):
            if i == 0:
                maxLengths.append(len(str(element)))
            else:
                length = len(str(element))
                if length > maxLengths[j]:
                    maxLengths[j] = length
    for reihe in list:
        newRow = []
        for n, number in enumerate(reihe):
            newRow.append(len(str(number)) - maxLengths[n] + 1)
        lengthList.append(newRow)
    return lengthList


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
        additionalSpaces = getNumbersLengthList(list)
        for i, row in enumerate(list):
            outputString = ""
            for j, element in enumerate(row):
                outputString += str(element)
                outputString += additionalSpaces[i][j]*" "
            print(outputString)


def isNotAVariable(s):
    for element in allMatrices:
        if element.name == s:
            return False
    return True


def isNotAMatrixType(s):
    for element in matrixArten:
        if element == s:
            return False
    return True


def calculateTerm(expression):
    if expression.__contains__("*"):
        a = expression.split("*")[0].strip()
        b = expression.split("*")[1].strip()
        aIsScalar = True
        numberOfScalars = 0
        if isNotAVariable(a) and isNotAMatrixType(a):
            a = int(a)
            numberOfScalars += 1
        elif isNotAVariable(a):
            a = MatrixGenerator().generateMatrix(a)
            aIsScalar = False
        else:
            a = getMatrix(a).value
            aIsScalar = False
        if isNotAVariable(b) and isNotAMatrixType(b):
            b = int(b)
            numberOfScalars += 1
        elif isNotAVariable(b):
            b = MatrixGenerator().generateMatrix(b)
        else:
            b = getMatrix(b).value
        if numberOfScalars < 2:
            if aIsScalar:
                return MatrixCalculator.scalarMultiply(a, b)
            else:
                return MatrixCalculator.scalarMultiply(b, a)
        else:
            return MatrixCalculator.matrixMultiply(a, b)
    elif expression.__contains__("+"):
        a = expression.split("+")[0].strip()
        b = expression.split("+")[1].strip()
        if isNotAVariable(a):
            a = MatrixGenerator().generateMatrix(a)
        else:
            a = getMatrix(a).value
        if isNotAVariable(b):
            b = MatrixGenerator().generateMatrix(b)
        else:
            b = getMatrix(b).value
        return MatrixCalculator.add(a, b)
    elif expression.__contains__("-"):
        a = expression.split("-")[0].strip()
        b = expression.split("-")[1].strip()
        if isNotAVariable(a):
            a = MatrixGenerator().generateMatrix(a)
        else:
            a = getMatrix(a).value
        if isNotAVariable(b):
            b = MatrixGenerator().generateMatrix(b)
        else:
            b = getMatrix(b).value
        return MatrixCalculator.minus(a, b)
    elif expression.__contains__("transp"):
        a = expression.split("(")[1].split(")")[0].strip()
        if isNotAVariable(a):
            a = MatrixGenerator().generateMatrix(a)
        else:
            a = getMatrix(a).value
        return MatrixCalculator.transponed(a)
    else:
        expression = expression.strip()
        if isNotAVariable(expression):
            return MatrixGenerator().generateMatrix(expression)
        else:
            return getMatrix(expression).value


def evaluateExpression(expression):
    matrix = Matrix("m")
    if expression.__contains__("=") == False:
        matrix.value = calculateTerm(expression)
        matrix.printMatrix()
    elif expression.__contains__("="):
        matrix.value = calculateTerm(expression.split("=")[1])
        matrix.name = expression.split("=")[0].strip()
        removeMatrix(matrix.name)
        allMatrices.append(matrix)


class MatrixCalculator:
    def add(a, b):
        if (len(a) == len(b)) and (len(a[0]) == len(b[0])):
            newValue = []
            for i, row in enumerate(a):
                newRow = []
                for j, number in enumerate(row):
                    newRow.append(number + b[i][j])
                newValue.append(newRow)
            return newValue
        else:
            print(
                "ERROR: FÜR DIE ADDITION ZWEIER MATRIZEN MÜSSEN DIE DIMENSIONEN ÜBEREINSTIMMEN")
            return None

    def minus(a, b):
        if (len(a) == len(b)) and (len(a[0]) == len(b[0])):
            newValue = []
            for i, row in enumerate(a):
                newRow = []
                for j, number in enumerate(row):
                    newRow.append(number - b[i][j])
                newValue.append(newRow)
            return newValue
        else:
            print(
                "ERROR: FÜR DIE ADDITION ZWEIER MATRIZEN MÜSSEN DIE DIMENSIONEN ÜBEREINSTIMMEN")
            return None

    def transpose(a):
        newValue = []
        for i in range(len(a[0])):
            newRow = []
            for row in a:
                newRow.append(row[i])
            newValue.append(newRow)
        return newValue

    def scalarMultiply(a, b):
        newValue = []
        for row in b:
            newRow = []
            for number in row:
                newRow.append(a*number)
            newValue.append(newRow)
        return newValue

    def matrixMultiply(a, b):
        return a


class MatrixGenerator:
    maxM = 8
    maxN = 8
    maxNumber = 9

    def userEnteredMatrix(_):
        dimensions = input("Gib die Dimensionen ein z.B.(5*3): ")
        stringList = []
        m = int(dimensions.split("*")[0])
        for i in range(m):
            row = input(f"Reihe {i + 1}: ")
            stringList.append(row)
        value = []
        for element in stringList:
            currentRow = []
            list = element.split(" ")
            for number in list:
                currentRow.append(int(number))
            value.append(currentRow)
        return value

    def symmetricMatrix(self, value, m):
        for i in range(m):
            for j in range(m):
                try:
                    a = value[j][i]
                    value[i].append(a)
                except:
                    value[i].append(random.randint(0, self.maxNumber))
        return value

    def upperTriangleMatrix(self, value, m):
        for i in range(m):
            for j in range(m):
                if j < i:
                    value[i].append(0)
                else:
                    value[i].append(random.randint(0, self.maxNumber))
        return value

    def lowerTriangleMatrix(self, value, m):
        for i in range(m):
            for j in range(m):
                if i < j:
                    value[i].append(0)
                else:
                    value[i].append(random.randint(0, self.maxNumber))
        return value

    def diagonalMatrix(self, value, m):
        for i in range(m):
            for j in range(m):
                if i == j:
                    value[i].append(random.randint(0, self.maxNumber))
                else:
                    value[i].append(0)
        return value

    def quadraticMatrix(self, value, m):
        for i in range(m):
            for j in range(m):
                value[i].append(random.randint(0, self.maxNumber))
        return value

    def identityMatrix(self, value, m):
        for i in range(m):
            for j in range(m):
                if i == j:
                    value[i].append(1)
                else:
                    value[i].append(0)
        return value

    def zeroMatrix(self, value, m, n):
        for i in range(m):
            for j in range(n):
                value[i].append(0)
        return value

    def generateMatrix(self, matrixType):
        if matrixType != "Benutzereingabe":
            import random
            m = random.randint(2, self.maxM)
            n = random.randint(2, self.maxN)
            value = []
            for _ in range(m):
                value.append([])
        match matrixType:
            case "Benutzereingabe":
                return self.userEnteredMatrix()
            case "symmetrischeMatrix":
                return self.symmetricMatrix(value, m)
            case "obereDreiecksmatrix":
                return self.upperTriangleMatrix(value, m)
            case "untereDreiecksmatrix":
                return self.lowerTriangleMatrix(value, m)
            case "Einheitsmatrix":
                return self.identityMatrix(value, m)
            case "Nullmatrix":
                return self.zeroMatrix(value, m, n)
            case "Diagonalmatrix":
                return self.diagonalMatrix(value, m)
            case "quadratischeMatrix":
                return self.quadraticMatrix(value, m)
            case _:
                print("ERROR: UNDEFINED MATRIX TYPE")
                return None


class TerminalSession:
    def interact(self):
        operation = input(">: ")
        evaluateExpression(operation)
        self.interact()


if __name__ == '__main__':
    TerminalSession().interact()
