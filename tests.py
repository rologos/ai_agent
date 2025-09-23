import unittest
from functions.run_python_file import run_python_file 

class TestGetFiles(unittest.TestCase):

    def test_1(self):
        result = run_python_file("calculator", "main.py")
        print(result)

    def test_2(self):
        result = run_python_file("calculator", "main.py", ["3 + 5"])
        print(result)

    def test_3(self):
        result = run_python_file("calculator", "tests.py")
        print(result)

    def test_4(self):
        result = run_python_file("calculator", "../main.py")
        print(result)
        self.assertIn("Error:",result)

    def test_5(self):
        result = run_python_file("calculator", "nonexistent.py")
        print(result)
        self.assertIn("Error:",result)

if __name__ == "__main__":
    unittest.main()
