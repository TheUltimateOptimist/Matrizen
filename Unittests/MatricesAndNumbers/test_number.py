from MatricesAndNumbers.number import Number
import unittest


class TestNumber(unittest.TestCase):
    def test_addNumber(self):
        self.assertAlmostEqual(Number(5.5).addNumber(Number(3.25)).value, 8.75)
        self.assertAlmostEqual(Number(-3.25).addNumber(Number(3.25)).value, 0)
        self.assertAlmostEqual(
            Number(-1000000).addNumber(Number(-1000000)).value, -2000000)

    def test_subtractNumber(self):
        self.assertAlmostEqual(
            Number(5.5).subtractNumber(Number(3.25)).value, 2.25)
        self.assertAlmostEqual(
            Number(-3.25).subtractNumber(Number(3.25)).value, -6.5)
        self.assertAlmostEqual(
            Number(-1000000).subtractNumber(Number(-1000000)).value, 0)

    def test_multiplyWithNumber(self):
        self.assertAlmostEqual(
            Number(5.5).multiplyWithNumber(Number(3.25)).value, 17.875)
        self.assertAlmostEqual(
            Number(-3.25).multiplyWithNumber(Number(3.25)).value, -10.5625)
        self.assertAlmostEqual(
            Number(-1000000).multiplyWithNumber(Number(-1000000)).value, 1000000000000)

    def test_divideByNumber(self):
        self.assertEqual(Number(-2.4).divideByNumber(Number(0)), None)
        self.assertAlmostEqual(
            Number(100).divideByNumber(Number(50)).value, 2.0)
        self.assertAlmostEqual(
            Number(-23.5).divideByNumber(Number(-34.34)).value, 0.6843331392)
        self.assertAlmostEqual(Number(23.5).divideByNumber(
            Number(-34.34)).value, -0.6843331392)

    def test_printNumber(self):
        self.assertEqual(Number(10).printNumber(), True)
        self.assertEqual(Number(0).printNumber(), True)
        self.assertEqual(Number(-34.34).printNumber(), True)

    def test_exponentiateByNumber(self):
        self.assertAlmostEqual(
            Number(10).exponentiateByNumber(Number(0)).value, 1)
        self.assertAlmostEqual(
            Number(-23.23).exponentiateByNumber(Number(1)).value, -23.23)
        self.assertAlmostEqual(
            Number(9).exponentiateByNumber(Number(0.5)).value, 3)
        self.assertAlmostEqual(
            Number(3.5).exponentiateByNumber(Number(5)).value, 525.21875)

    def test_takeSquareRoot(self):
        self.assertAlmostEqual(Number(0).takeSquareRoot().value, 0)
        self.assertAlmostEqual(Number(225).takeSquareRoot().value, 15)
        self.assertAlmostEqual(Number(2.5).takeSquareRoot().value, 1.58113883)
        self.assertAlmostEqual(Number(-7).takeSquareRoot(), None)
