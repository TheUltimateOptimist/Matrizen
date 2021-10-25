from littleFunctions.color import printRed, printBlue
from language import matrixChecks


class Attributes:
    attributes = matrixChecks

    def isAttribute(self, attribute):
        for element in self.attributes:
            if element == attribute:
                return True
        return False

    def check(self, variable, attribute):
        if str(variable.__class__) == "<class 'MatricesAndNumbers.matrix.Matrix'>":
            match attribute:
                case "symmetrisch":
                    return variable.isSymmetricMatrix()
                case "quadratisch":
                    return variable.isQuadraticMatrix()
                case "Einheitsmatrix":
                    return variable.isIdentityMatrix()
                case "Diagonalmatrix":
                    return variable.isDiagonalMatrix()
                case "Nullmatrix":
                    return variable.isNullMatrix()
                case "untereDreiecksmatrix":
                    return variable.isLowerTriangleMatrix()
                case "obereDreiecksmatrix":
                    return variable.isUpperTriangleMatrix()
                case "invertierbar":
                    return variable.isInvertableMatrix()
                case "Eigenschaften":
                    attributes = variable.getAttributes()
                    for attribute in attributes:
                        printBlue(attribute)
                    return attributes
                case _:
                    printRed(
                        f"ERROR: DIE OPERATION {attribute} IST FÜR DIE KLASSE MATRIX NICHT DEFINIERT!")
        elif str(variable.__class__) == "<class '__main__.Number'>":
            printRed(
                f"ERROR: DER BEFEHL {attribute} IST FÜR ZAHLEN NICHT DEFINIERT!")
            return None
        else:
            printRed(
                f"ERROR: DIE OPERATION {attribute} IST FÜR DIE KLASSE {variable.__class__} NICHT DEFINIERT!")
