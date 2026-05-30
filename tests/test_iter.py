import unittest
from kirilltools.errors import iter as itererr
from kirilltools.Utils import iter as iter_

class IterTest(unittest.TestCase):
    def test_genchank_success(self):
        self.assertEqual(iter_.gen_chank([1, 2, 3, 4, 5, 6], 2), [[1, 2], [3, 4], [5, 6]])
        self.assertIsInstance(iter_.gen_chank([1, 2], 1), list)
    def test_genchank_error(self):
        with self.assertRaises(itererr.SizeLessZero):
            iter_.gen_chank([0], -1)
        with self.assertRaises(itererr.NotAListError):
            iter_.gen_chank(5, 1)
    def test_listflattening_success(self):
        self.assertEqual(iter_.list_flattening([[1, 3], [4, 6]]), [1, 3, 4, 6])
        self.assertIsInstance(iter_.list_flattening([]), list)
    def test_listflatteing_error(self):
        with self.assertRaises(itererr.NotAListError):
            iter_.list_flattening(5)
        with self.assertRaises(itererr.NotListInListError):
            iter_.list_flattening([2, 4])
if __name__ == "__main__":
    unittest.main()