import unittest
from MatricesAndNumbers.matrixGenerator import MatrixGenerator


class TestMatrixGenerator(unittest.TestCase):
    def setUp(self):
        self.smallGenerator = MatrixGenerator()
        self.smallGenerator.maxM = 5
        self.smallGenerator.maxN = 5
        self.smallGenerator.maxNumber = 9
        self.bigGenerator = MatrixGenerator()
        self.bigGenerator.maxNumber = 1000000
        self.bigGenerator.maxM = 30
        self.bigGenerator.maxN = 30
    def test_generateMatrix(self):
        self.assertTrue(self.smallGenerator.generateMatrix("symmetrischeMatrix").isSymmetricMatrix())
        self.assertTrue(self.smallGenerator.generateMatrix("obereDreiecksmatrix").isUpperTriangleMatrix())
        self.assertTrue(self.smallGenerator.generateMatrix("untereDreiecksmatrix").isLowerTriangleMatrix())
        self.assertTrue(self.smallGenerator.generateMatrix("Einheitsmatrix").isIdentityMatrix())
        self.assertTrue(self.smallGenerator.generateMatrix("Nullmatrix").isNullMatrix())
        self.assertTrue(self.smallGenerator.generateMatrix("Diagonalmatrix").isDiagonalMatrix())
        self.assertTrue(self.smallGenerator.generateMatrix("quadratischeMatrix").isQuadraticMatrix())
        self.assertTrue(self.bigGenerator.generateMatrix("symmetrischeMatrix").isSymmetricMatrix())
        self.assertTrue(self.bigGenerator.generateMatrix("obereDreiecksmatrix").isUpperTriangleMatrix())
        self.assertTrue(self.bigGenerator.generateMatrix("untereDreiecksmatrix").isLowerTriangleMatrix())
        self.assertTrue(self.bigGenerator.generateMatrix("Einheitsmatrix").isIdentityMatrix())
        self.assertTrue(self.bigGenerator.generateMatrix("Nullmatrix").isNullMatrix())
        self.assertTrue(self.bigGenerator.generateMatrix("Diagonalmatrix").isDiagonalMatrix())
        self.assertTrue(self.bigGenerator.generateMatrix("quadratischeMatrix").isQuadraticMatrix())