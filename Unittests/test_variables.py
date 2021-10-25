import unittest
from variables import Variables

class TestVariables(unittest.TestCase):
    def setUp(self):
        self.variables = Variables()
        self.variables.names = ["Hallo", "A", "a", "Auto", "b"]
        self.variables.values = ["hass", 3, -2.34, "kdsj", []]

    def test_add(self):
        self.variables.add("Z", "skdjk")
        self.assertEqual(self.variables.names[len(self.variables.names) - 1], "Z") 
        self.assertEqual(self.variables.values[len(self.variables.values) - 1], "skdjk")  

    def test_remove(self):
        self.variables.remove("Hallo")
        self.assertEqual(self.variables.names[0], "A")
        self.assertEqual(self.variables.values[0], 3)

    def test_contains(self):
        self.assertTrue(self.variables.contains("Auto"))
        self.assertFalse(self.variables.contains("Autos"))

    def test_getValue(self):
        self.assertEqual(self.variables.getValue("a"), -2.34)
        self.assertEqual(self.variables.getValue("Auto"), "kdsj")
        self.assertEqual(self.variables.getValue("sdjfsdfjsdfjsdjf"), None)    
