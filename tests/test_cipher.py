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
    def test_vigenere_cipher_success(self):
        self.assertEqual(cipher.Vigenere_cipher("abc", [3, 3, 3]), "def")
        self.assertEqual(cipher.Vigenere_cipher("abc", str(chr(3)) * 3), "def")
    def test_vigenere_cipher_error(self):
        with self.assertRaises(matherr.TypesError):
            cipher.Vigenere_cipher("abc", 4)
        with self.assertRaises(ciphererr.KeyFormatError):
            cipher.Vigenere_cipher("abc", [3, 2, "B"])
    def test_uncode_vigenere_cipher_error(self):
        with self.assertRaises(matherr.TypesError):
            cipher.Uncode_Vigenere_cipher("def", 2)
        with self.assertRaises(ciphererr.KeyFormatError):
            cipher.Uncode_Vigenere_cipher("def", [3, 3, "A"])

if __name__ == "__main__":
    unittest.main()