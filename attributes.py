from color import printRed, printBlue
from language import matrixChecks


class Attributes:
    attributes = matrixChecks

    def isAttribute(self, attribute):
        for element in self.attributes:
            if element == attribute:
                return True
        return False

    def check(self, variable, attribute):
        if variable.__class__ == "<class '__main__.Matrix'>":
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
                    for element in variable.getAttributes():
                        printBlue(element)
                    return ""
                case _:
                    printRed(
                        f"ERROR: DIE OPERATION {attribute} IST FÜR DIE KLASSE MATRIX NICHT DEFINIERT!")
        elif variable.__class__ == "<class '__main__.Number'>":
            printRed(
                f"ERROR: DER BEFEHL {attribute} IST FÜR ZAHLEN NICHT DEFINIERT!")
            return None
        else:
            printRed(
                f"ERROR: DIE OPERATION {attribute} IST FÜR DIE KLASSE {variable.__class__} NICHT DEFINIERT!")
