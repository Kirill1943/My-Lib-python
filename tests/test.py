import unittest

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.discover(start_dir="tests", pattern="test_*.py")
    
    runner = unittest.TextTestRunner()
    runner.run(suite)