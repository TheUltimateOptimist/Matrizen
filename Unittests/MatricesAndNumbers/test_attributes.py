from MatricesAndNumbers.attributes import Attributes
from MatricesAndNumbers.matrix import Matrix
import unittest
from language import matrixChecks

class TestAttributes(unittest.TestCase):
    def setUp(self):
        self.matrixThree = Matrix(
            [[4, 5, -2, 1000], [3, 2, 3.2, 7], [100000, 2, -2.34, 9]])
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
    def test_isAttribute(self):
        for check in matrixChecks:
            self.assertTrue(Attributes().isAttribute(check))
        self.assertFalse(Attributes().isAttribute("hallo"))
        self.assertFalse(Attributes().isAttribute(34))

    def test_check(self):
        self.assertTrue(Attributes().check(self.quadraticMatrix, "quadratisch"))
        self.assertFalse(Attributes().check(self.matrixThree, "quadratisch"))  
        self.assertTrue(Attributes().check(self.upperTriangleMatrix, "obereDreiecksmatrix"))
        self.assertFalse(Attributes().check(self.lowerTriangleMatrix, "obereDreiecksmatrix"))
        self.assertFalse(Attributes().check(self.matrixThree, "obereDreiecksmatrix"))
        self.assertTrue(Attributes().check(self.identityMatrix, "obereDreiecksmatrix"))
        self.assertFalse(Attributes().check(self.upperTriangleMatrix, "untereDreiecksmatrix"))
        self.assertTrue(Attributes().check(self.lowerTriangleMatrix, "untereDreiecksmatrix"))
        self.assertFalse(Attributes().check(self.matrixThree, "untereDreiecksmatrix"))
        self.assertTrue(Attributes().check(self.identityMatrix, "untereDreiecksmatrix"))
        self.assertFalse(Attributes().check(self.matrixThree, "Einheitsmatrix"))
        self.assertFalse(Attributes().check(self.upperTriangleMatrix, "Einheitsmatrix"))
        self.assertTrue(Attributes().check(self.identityMatrix, "Einheitsmatrix"))
        self.assertFalse(Attributes().check(self.nullMatrix, "Einheitsmatrix"))
        self.assertTrue(Attributes().check(self.nullMatrix, "Nullmatrix"))
        self.assertFalse(Attributes().check(self.identityMatrix, "Nullmatrix"))
        self.assertFalse(Attributes().check(self.matrixThree, "Nullmatrix"))
        self.assertTrue(Attributes().check(self.diagonalMatrix, "Diagonalmatrix"))
        self.assertFalse(Attributes().check(self.upperTriangleMatrix, "Diagonalmatrix"))
        self.assertFalse(Attributes().check(self.matrixThree, "Diagonalmatrix"))
        self.assertFalse(Attributes().check(self.nullMatrix, "Diagonalmatrix"))
        self.assertFalse(Attributes().check(self.matrixThree, "symmetrisch"))
        self.assertFalse(Attributes().check(self.quadraticMatrix, "symmetrisch"))
        self.assertTrue(Attributes().check(self.symmetricMatrix, "symmetrisch"))
        # self.assertFalse(Attributes().check(self.quadraticMatrix, "invertierbar"))
        # self.assertFalse(Attributes().check(self.invertableMatrix,"invertierbar"))
        # self.assertFalse(Attributes().check(self.matrixThree, "invertierbar"))
        # also invertable
        self.assertEqual(Attributes().check(self.identityMatrix, "Eigenschaften"), [
                         "quadratisch", "symmetrisch", "Einheitsmatrix", "Diagonalmatrix", "obere Dreiecksmatrix", "untere Dreiecksmatrix"])
        # also invertable
        self.assertEqual(Attributes().check(self.upperTriangleMatrix, "Eigenschaften"), [
                         "quadratisch", "obere Dreiecksmatrix"])
        # also invertable
        self.assertEqual(Attributes().check(self.lowerTriangleMatrix, "Eigenschaften"), [
                         "quadratisch", "untere Dreiecksmatrix"])
        self.assertEqual(Attributes().check(self.nullMatrix, "Eigenschaften"), ["Nullmatrix"])
        # also invertable
        self.assertEqual(Attributes().check(self.diagonalMatrix, "Eigenschaften"), [
                         "quadratisch", "symmetrisch", "Diagonalmatrix", "obere Dreiecksmatrix", "untere Dreiecksmatrix"])

