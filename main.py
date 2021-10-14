from matrix import Matrix
from matrixCalculator import MatrixCalculator
from matrixGenerator import MatrixGenerator
from matrixContainer import MatrixContainer


def calculateTerm(expression, matrixContainer):
    if expression.__contains__("*"):
        a = expression.split("*")[0].strip()
        b = expression.split("*")[1].strip()
        aIsScalar = True
        numberOfScalars = 0
        if matrixContainer.notContainsMatrix(a) and matrixContainer.notContainsMatrixArt(a):
            a = int(a)
            numberOfScalars += 1
        elif matrixContainer.notContainsMatrix(a):
            a = MatrixGenerator().generateMatrix(a)
            aIsScalar = False
        else:
            a = matrixContainer.getMatrix(a).value
            aIsScalar = False
        if matrixContainer.notContainsMatrix(b) and matrixContainer.notContainsMatrixArt(b):
            b = int(b)
            numberOfScalars += 1
        elif matrixContainer.notContainsMatrix(b):
            b = MatrixGenerator().generateMatrix(b)
        else:
            b = matrixContainer.getMatrix(b).value
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
        if matrixContainer.notContainsMatrix(a):
            a = MatrixGenerator().generateMatrix(a)
        else:
            a = matrixContainer.getMatrix(a).value
        if matrixContainer.notContainsMatrix(b):
            b = MatrixGenerator().generateMatrix(b)
        else:
            b = matrixContainer.getMatrix(b).value
        return MatrixCalculator.add(a, b)
    elif expression.__contains__("-"):
        a = expression.split("-")[0].strip()
        b = expression.split("-")[1].strip()
        if matrixContainer.notContainsMatrix(a):
            a = MatrixGenerator().generateMatrix(a)
        else:
            a = matrixContainer.getMatrix(a).value
        if matrixContainer.notContainsMatrix(b):
            b = MatrixGenerator().generateMatrix(b)
        else:
            b = matrixContainer.getMatrix(b).value
        return MatrixCalculator.minus(a, b)
    elif expression.__contains__("transp"):
        a = expression.split("(")[1].split(")")[0].strip()
        if matrixContainer.notContainsMatrix(a):
            a = MatrixGenerator().generateMatrix(a)
        else:
            a = matrixContainer.getMatrix(a).value
        return MatrixCalculator.transponed(a)
    elif expression.__contains__("."):
        a = expression.split(".")[0].strip()
        a = matrixContainer.getMatrix(a)
        type = expression.split(".")[1].strip()
        match type:
            case "Eigenschaften":
                eigenschaften = a.getProperties()
                print("Eigenschaften: ")
                for element in eigenschaften:
                    print(element)
            case "symmetrischeMatrix":
                if a.isSymmetricMatrix():
                    print("True")
                else:
                    print("False")
            case "obereDreiecksmatrix":
                if a.isUpperTriangleMatrix():
                    print("True")
                else:
                    print("False")
            case "untereDreiecksmatrix":
                if a.isLowerTriangleMatrix():
                    print("True")
                else:
                    print("False")
            case "Einheitsmatrix":
                if a.isIdentityMatrix():
                    print("True")
                else:
                    print("False")
            case "Nullmatrix":
                if a.isNullMatrix():
                    print("True")
                else:
                    print("False")
            case "Diagonalmatrix":
                if a.isDiagonalMatrix():
                    print("True")
                else:
                    print("False")
            case "quadratischeMatrix":
                if a.isQuadraticMatrix():
                    print("True")
                else:
                    print("False")
            case _:
                print(f"ERROR: EIGENSCHAFT {type} NOT FOUND")
        return None
    else:
        expression = expression.strip()
        if matrixContainer.notContainsMatrix(expression):
            if matrixContainer.containsMatrixArt(expression):
                return MatrixGenerator().generateMatrix(expression)
            else:
                print("ERROR: UNKNOWN EXPRESSION")
                return None
        else:
            return matrixContainer.getMatrix(expression).value


def evaluateExpression(expression, matrixContainer):
    matrix = Matrix("m")
    if expression.__contains__("=") == False:
        expressionResult = calculateTerm(expression, matrixContainer)
        if expressionResult != None:
            matrix.value = expressionResult
            matrix.printMatrix()
    elif expression.__contains__("="):
        matrix.value = calculateTerm(expression.split("=")[1], matrixContainer)
        matrix.name = expression.split("=")[0].strip()
        matrixContainer.removeMatrix(matrix.name)
        matrixContainer.add(matrix)


class TerminalSession:
    matrixContainer = MatrixContainer()

    def interact(self):
        operation = input(">: ")
        evaluateExpression(operation, self.matrixContainer)
        self.interact()


if __name__ == '__main__':
    TerminalSession().interact()
