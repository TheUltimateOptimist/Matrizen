import unittest
from variables import Variables

class TestVariables(unittest.TestCase):
    def setUp(self):
        Variables.names = ["Hallo", "A", "a", "Auto", "b"]
        Variables.values = ["hass", 3, -2.34, "kdsj", []]

    def test_add(self):
        Variables().add("Z", "skdjk")
        self.assertEqual(Variables.names[len(Variables().names) - 1], "Z") 
        self.assertEqual(Variables.values[len(Variables().values) - 1], "skdjk")  

    def test_remove(self):
        Variables().remove("Hallo")
        self.assertEqual(Variables.names[0], "A")
        self.assertEqual(Variables.values[0], 3)

    def test_contains(self):
        self.assertTrue(Variables.contains("Auto"))
        self.assertFalse(Variables.contains("Autos"))

    def test_getValue(self):
        self.assertEqual(Variables.getValue("a"), -2.34)
        self.assertEqual(Variables.getValue("Auto"), "kdsj")
        self.assertEqual(Variables.getValue("sdjfsdfjsdfjsdjf"), None)    
