import unittest
from littleFunctions.mathFunctions import isNumber, contains, getClosingBraceIndex

class TestMathFunctions(unittest.TestCase):
    def test_isNumber(self):
        self.assertFalse(isNumber("kdjf"))
        self.assertFalse(isNumber("))"))
        self.assertTrue(isNumber("-3.344553"))
        self.assertTrue(isNumber("34343434"))
        self.assertTrue(isNumber("+34.34"))

    def test_contains(self):
        self.assertFalse(contains("kdsjfksdfjksdfljsdfdfhjsdsdhfashsdjf3245823498wf", ["haus",  "ssssss"]))
        self.assertFalse(contains("dkfjk", []))
        self.assertTrue(contains("ich hei384928 Jonathan", ["Jonathan"]))

    def test_getClosingBraceIndex(self):
        self.assertEqual(getClosingBraceIndex(0, ["(", "(", "(", ")", ")", ")"]), 5)  
        self.assertEqual(getClosingBraceIndex(1, ["(", "(", "a","^",")", ")"]), 4)  