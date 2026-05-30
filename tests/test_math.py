import unittest
from kirilltools import Math
from kirilltools.errors import math as matherr

class TestModule(unittest.TestCase):
    def test_getkilo_success(self):
        self.assertEqual(Math.get_kilo(5, 10), 50.0)
        self.assertIsInstance(Math.get_kilo(5, 10), float)
    def test_getkilo_error(self):
        with self.assertRaises(matherr.TypesError):
            Math.get_kilo("", 3)
    def test_double_factorial_success(self):
        self.assertEqual(Math.double_factorial(10), 3840)
        self.assertIsInstance(Math.double_factorial(1), int)
        self.assertEqual(Math.double_factorial(0), 1)
    def test_tetration_success(self):
        self.assertEqual(Math.tetration(1, 0), 1)
    def test_tetration_error(self):
        with self.assertRaises(matherr.TypesError):
            Math.tetration("", "")
    def test_fib_success(self):
        self.assertIsInstance(Math.fib(1), list)
        self.assertEqual(Math.fib(4), [1, 2, 3, 5])
    def test_fib_error(self):
        with self.assertRaises(matherr.TypesError):
            Math.fib("")
if __name__ == "__main__":
    unittest.main()