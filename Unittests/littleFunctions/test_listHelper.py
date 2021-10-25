import unittest
from littleFunctions.listHelper import split_list, delete_range, getNumbersLengthList

class TestListHelper(unittest.TestCase):
    def setUp(self):
        pass
    def test_split_list(self):
        self.assertEqual(split_list(2, 5, [1,2,3,4,5,6,7,8]), [3,4,5,6])
        self.assertEqual(split_list(1,2, [[1], [2], [3], [4], []]), [[2], [3]])

    def test_delete_range(self):
        self.assertEqual(delete_range(2,5,[1,2,3,4,5,6,7,8]), [1,2,7,8])  
        self.assertEqual(delete_range(1,2, [[1], [2], [3], [4]]), [[1], [4]])  

    def test_getNumbersLengthList(self):
        self.assertEqual(getNumbersLengthList([[2, 23000, 4], [234.3, 5, -4000000]]), [[5, 1, 8], [1, 5, 1]])    
    