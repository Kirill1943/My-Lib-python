import unittest
from kirilltools.errors import cipherError as ciphererr, math as matherr
from kirilltools import cipher

class CipherTest(unittest.TestCase):
    def test_cipher_error(self):
        with self.assertRaises(matherr.TypesError):
            cipher.Caesar_cipher("abcd", "")
        with self.assertRaises(matherr.TypesError):
            cipher.Super_Caesar_Cipher("abcd", "", "")
    def test_cipher_and_supercipher_success(self):
        self.assertEqual(cipher.Caesar_cipher("hello world!", 16), "xu||\x7f0\x87\x7f\x82|t1")
        self.assertEqual(cipher.Super_Caesar_Cipher("hello world!", 2, 8), "xu||\x7f0\x87\x7f\x82|t1")
        self.assertIsInstance(cipher.Caesar_cipher("", 1), str)
        self.assertIsInstance(cipher.Super_Caesar_Cipher("", 1, 1), str)
    def test_cipher_and_supercipher_uncode_success(self):
        self.assertEqual(cipher.uncoding_caesar_cipher("xu||\x7f0\x87\x7f\x82|t1", 16), "hello world!")
    def test_keys_success(self):
        self.assertIsInstance(cipher.keys(), dict)
        self.assertIsNotNone(cipher.keys())


if __name__ == "__main__":
    unittest.main()