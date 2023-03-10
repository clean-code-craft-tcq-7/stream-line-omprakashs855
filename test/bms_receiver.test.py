""" This file contains test methods """
import unittest

def run_tests():
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir="test", pattern="t_*.py")
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    return result

if __name__ == "__main__":
    run_tests()