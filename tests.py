import unittest
from functions.get_files_info import get_files_info 

class TestGetFiles(unittest.TestCase):

    def test_get_parent(self):
        print(f"Result for \'../\' directory:")
        result = get_files_info("calculator", "../")
        self.assertIn("Error:",result)

    def test_current(self):
        print(f"Result for current directory:")
        result = get_files_info("calculator", ".")
        self.assertIn("tests.py",result)
        self.assertIn("main.py",result)
        self.assertIn("is_dir=False",result)
        self.assertIn("is_dir=True",result)

'''
    def test_get_current(self):

        self.assertEqual(result, 8)
    def test_get_pkg(self):
        result = self.calculator.evaluate("10 - 4")
        self.assertEqual(result, 6)

    def test_get_bin(self):
        result = self.calculator.evaluate("3 * 4")
        self.assertEqual(result, 12)

    def test_not_enough_operands(self):
        with self.assertRaises(ValueError):
            self.calculator.evaluate("+ 3")
'''

if __name__ == "__main__":
    unittest.main()
