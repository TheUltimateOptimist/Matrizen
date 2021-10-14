class MatrixContainer:
    matrixArten = ["Benutzereingabe", "symmetrischeMatrix", "obereDreiecksmatrix",
                   "untereDreiecksmatrix", "Einheitsmatrix", "Nullmatrix", "Diagonalmatrix", "quadratischeMatrix"]

    def __init__(self):
        self.allMatrices = []

    def removeMatrix(self, name):
        for matrix in self.allMatrices:
            if matrix.name == name:
                self.allMatrices.remove(matrix)
                break

    def getMatrix(self, name):
        for element in self.allMatrices:
            if element.name == name:
                return element
        return None

    def add(self, matrix):
        self.allMatrices.append(matrix)

    def notContainsMatrix(self, matrixName):
        for matrix in self.allMatrices:
            if matrix.name == matrixName:
                return False
        return True

    def notContainsMatrixArt(self, matrixArt):
        for element in self.matrixArten:
            if element == matrixArt:
                return False
        return True

    def containsMatrix(self, matrix):
        if self.notContainsMatrix(matrix):
            return False
        else:
            return True

    def containsMatrixArt(self, matrixArt):
        if self.notContainsMatrixArt(matrixArt):
            return False
        else:
            return True
