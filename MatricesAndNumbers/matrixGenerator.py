from littleFunctions.randomNumbers import randomNumber
from MatricesAndNumbers.matrix import Matrix


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
        return Matrix(value)

    def symmetricMatrix(self, value, m):
        for i in range(m):
            for j in range(m):
                try:
                    a = value[j][i]
                    value[i].append(a)
                except:
                    value[i].append(randomNumber(self.maxNumber))
        return Matrix(value)

    def upperTriangleMatrix(self, value, m):
        for i in range(m):
            for j in range(m):
                if j < i:
                    value[i].append(0)
                else:
                    value[i].append(randomNumber(self.maxNumber))
        return Matrix(value)

    def lowerTriangleMatrix(self, value, m):
        for i in range(m):
            for j in range(m):
                if i < j:
                    value[i].append(0)
                else:
                    value[i].append(randomNumber(self.maxNumber))
        return Matrix(value)

    def diagonalMatrix(self, value, m):
        for i in range(m):
            for j in range(m):
                if i == j:
                    value[i].append(randomNumber(self.maxNumber))
                else:
                    value[i].append(0)
        return Matrix(value)

    def quadraticMatrix(self, value, m):
        for i in range(m):
            for j in range(m):
                value[i].append(randomNumber(self.maxNumber))
        return Matrix(value)

    def identityMatrix(self, value, m):
        for i in range(m):
            for j in range(m):
                if i == j:
                    value[i].append(1)
                else:
                    value[i].append(0)
        return Matrix(value)

    def zeroMatrix(self, value, m, n):
        for i in range(m):
            for j in range(n):
                value[i].append(0)
        return Matrix(value)

    def randomMatrix(self, value, m, n):
        for i in range(m):
            for _ in range(n):
                value[i].append(randomNumber(self.maxNumber, includeZero=True))
        return Matrix(value)

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
            case "ZufallsMatrix":
                return self.randomMatrix(value, m, n)
            case _:
                return None
