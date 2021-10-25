import unittest
from littleFunctions.randomNumbers import randomNumber    

class TestRandomNumbers(unittest.TestCase):
    def test_randomNumber(self):
        rightBorder = 10
        for _ in range(rightBorder*10):
            self.assertLessEqual(abs(randomNumber(rightBorder)), rightBorder)
            self.assertNotEqual(abs(randomNumber(rightBorder)), 0)
        self.assertEqual(abs(randomNumber(0, includeZero=True)), 0)