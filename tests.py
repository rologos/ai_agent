import unittest
from functions.get_files_info import get_files_info 

class TestGetFiles(unittest.TestCase):

    def test_get_parent(self):
        print(f"Result for \'../\' directory:")
        result = get_files_info("calculator", "../")
        print(result)
        self.assertIn("Error:",result)

    def test_current(self):
        print(f"Result for current directory:")
        result = get_files_info("calculator", ".")
        print(result)
        self.assertIn("tests.py",result)
        self.assertIn("main.py",result)
        self.assertIn("is_dir=False",result)
        self.assertIn("is_dir=True",result)

    def test_pkg(self):
        print(f"Result for \'pkg\' directory:")
        result = get_files_info("calculator", "pkg")
        print(result)
        self.assertIn("render.py",result)
        self.assertIn("calculator.py",result)

    def test_bin(self):
        print(f"Result for \'/bin\' directory:")
        result = get_files_info("calculator", "/bin")
        print(result)
        self.assertIn("Error:",result)

if __name__ == "__main__":
    unittest.main()
