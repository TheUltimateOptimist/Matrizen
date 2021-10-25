import unittest
from MatricesAndNumbers.matrix import Matrix
from MatricesAndNumbers.number import Number


class TestMatrix(unittest.TestCase):
    def setUp(self):
        self.emptyMatrix = Matrix([])
        self.matrixTwo = Matrix([[3], [8]])
        self.matrixThree = Matrix(
            [[4, 5, -2, 1000], [3, 2, 3.2, 7], [100000, 2, -2.34, 9]])
        self.matrixFour = Matrix([[8, 7, -4], [12, 3, 2.5]])
        self.matrixFive = Matrix([[8, 5, -3], [100, 1000000, 1]])
        self.matrixSix = Matrix([[16, 12, -7], [112, 1000003, 3.5]])
        self.quadraticMatrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.upperTriangleMatrix = Matrix([[7, 8, 3], [0, 5, 6], [0, 0, 10]])
        self.lowerTriangleMatrix = Matrix(
            [[2, 0, 0], [8, 20, 0], [-10, 2.5, -3.5]])
        self.identityMatrix = Matrix(
            [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        self.nullMatrix = Matrix([[0, 0, 0, 0, 0, ], [0, 0, 0, 0, 0]])
        self.diagonalMatrix = Matrix([[1, 0, 0], [0, -12.5, 0], [0, 0, 10000]])
        self.symmetricMatrix = Matrix(
            [[12, 3, 10], [3, 13, 10000], [10, 10000, -4.5]])
        self.invertableMatrix = Matrix([[2, 4, 10], [8, 6, 8], [20, 4, 2]])

    def test_getDimensions(self):
        self.assertEqual(self.emptyMatrix.getDimensions(), [0, 0])
        self.assertEqual(self.matrixTwo.getDimensions(), [2, 1])
        self.assertEqual(self.matrixThree.getDimensions(), [3, 4])

    def test_getMatrixSum(self):
        self.assertEqual(self.emptyMatrix.getMatrixSum().value, 0)
        self.assertEqual(self.matrixThree.getMatrixSum().value, 101030.86)

    def test_printMatrix(self):
        self.assertEqual(self.emptyMatrix.printMatrix(), True)
        self.assertEqual(self.matrixThree.printMatrix(), True)

    def test_addMatrix(self):
        self.assertEqual(self.matrixTwo.addMatrix(self.matrixThree), None)
        self.assertEqual(self.matrixFour.addMatrix(
            self.matrixFive).value, self.matrixSix.value)

    def test_subtractMatrix(self):
        self.assertEqual(self.matrixTwo.subtractMatrix(self.matrixThree), None)
        self.assertEqual(self.matrixFour.subtractMatrix(
            self.matrixFive).value, [[0, 2, -1], [-88, -999997, 1.5]])

    def test_multiplyWithMatrix(self):
        pass
        # self.assertEqual(self.matrixTwo.multiplyWithMatrix(self.matrixThree), None)
        # self.assertEqual(self.matrixFour.multiplyWithMatrix(self.matrixThree).value, [[-399947, 46, 17.86, 8013], [250057, 71, -20.25, 12043.5]])

    def test_divideByMatrix(self):
        # implement later
        pass

    def test_exponentiateByNumber(self):
        # implement later
        pass

    def test_multiplyWithNumber(self):
        self.assertEqual(
            self.matrixTwo.multiplyWithNumber(Number(4)).value, [[12], [32]])
        self.assertEqual(
            self.emptyMatrix.multiplyWithNumber(Number(3.4)).value, [])
        self.assertEqual(self.matrixFour.multiplyWithNumber(
            Number(2.5)).value, [[20, 17.5, -10], [30, 7.5, 6.25]])

    def test_divideByNumber(self):
        self.assertEqual(self.matrixTwo.divideByNumber(
            Number(4)).value, [[0.75], [2]])
        self.assertEqual(
            self.emptyMatrix.divideByNumber(Number(3.4)).value, [])
        self.assertEqual(self.matrixFour.divideByNumber(
            Number(0.4)).value, [[20, 17.5, -10], [30, 7.5, 6.25]])

    def test_transpose(self):
        self.assertEqual(self.matrixTwo.transpose().value, [[3, 8]])
        self.assertEqual(self.emptyMatrix.transpose().value, [])
        self.assertEqual(self.matrixThree.transpose().value, [
                         [4, 3, 100000], [5, 2, 2], [-2, 3.2, -2.34], [1000, 7, 9]])

    def test_invert(self):
        pass
        # self.assertEqual(self.emptyMatrix.invert().value, None)
        # self.assertEqual(self.matrixThree.invert().value, None)
        # self.assertEqual(self.quadraticMatrix, None)
        # self.assertAlmostEqual(self.invertableMatrix.invert().value, [
        #                        [5/86, -4/43, 7/86], [-18/43, 49/86, -8/43], [11/43, -9/43, 5/86]])

    def test_isQuadraticMatrix(self):
        self.assertTrue(self.quadraticMatrix.isQuadraticMatrix())
        self.assertFalse(self.matrixThree.isQuadraticMatrix())

    def test_isUpperTriangleMatrix(self):
        self.assertTrue(self.upperTriangleMatrix.isUpperTriangleMatrix())
        self.assertFalse(self.lowerTriangleMatrix.isUpperTriangleMatrix())
        self.assertFalse(self.matrixThree.isUpperTriangleMatrix())
        self.assertTrue(self.identityMatrix.isUpperTriangleMatrix())

    def test_isLowerTriangleMatrix(self):
        self.assertFalse(self.upperTriangleMatrix.isLowerTriangleMatrix())
        self.assertTrue(self.lowerTriangleMatrix.isLowerTriangleMatrix())
        self.assertFalse(self.matrixThree.isLowerTriangleMatrix())
        self.assertTrue(self.identityMatrix.isLowerTriangleMatrix())

    def test_isIdentityMatrix(self):
        self.assertFalse(self.matrixThree.isIdentityMatrix())
        self.assertFalse(self.upperTriangleMatrix.isIdentityMatrix())
        self.assertTrue(self.identityMatrix.isIdentityMatrix())
        self.assertFalse(self.nullMatrix.isIdentityMatrix())

    def test_isNullMatrix(self):
        self.assertTrue(self.nullMatrix.isNullMatrix())
        self.assertFalse(self.identityMatrix.isNullMatrix())
        self.assertFalse(self.matrixThree.isNullMatrix())

    def test_isDiagonalMatrix(self):
        self.assertTrue(self.diagonalMatrix.isDiagonalMatrix())
        self.assertFalse(self.upperTriangleMatrix.isDiagonalMatrix())
        self.assertFalse(self.matrixThree.isDiagonalMatrix())
        self.assertFalse(self.nullMatrix.isDiagonalMatrix())

    def test_isSymmetricMatrix(self):
        self.assertFalse(self.matrixThree.isSymmetricMatrix())
        self.assertFalse(self.quadraticMatrix.isSymmetricMatrix())
        self.assertTrue(self.symmetricMatrix.isSymmetricMatrix())

    def test_isInvertableMatrix(self):
        pass
        # self.assertFalse(self.quadraticMatrix.isInvertableMatrix())
        # self.assertFalse(self.invertableMatrix.isInvertableMatrix())
        # self.assertFalse(self.matrixThree.isInvertableMatrix())

    def test_getAttributes(self):
        # also invertable
        self.assertEqual(self.identityMatrix.getAttributes(), [
                         "quadratisch", "symmetrisch", "Einheitsmatrix", "Diagonalmatrix", "obere Dreiecksmatrix", "untere Dreiecksmatrix"])
        # also invertable
        self.assertEqual(self.upperTriangleMatrix.getAttributes(), [
                         "quadratisch", "obere Dreiecksmatrix"])
        # also invertable
        self.assertEqual(self.lowerTriangleMatrix.getAttributes(), [
                         "quadratisch", "untere Dreiecksmatrix"])
        self.assertEqual(self.nullMatrix.getAttributes(), ["Nullmatrix"])
        # also invertable
        self.assertEqual(self.diagonalMatrix.getAttributes(), [
                         "quadratisch", "symmetrisch", "Diagonalmatrix", "obere Dreiecksmatrix", "untere Dreiecksmatrix"])
