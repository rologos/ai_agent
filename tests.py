import unittest
from functions.get_files_info import get_files_info 
from functions.get_file_content import get_file_content 

class TestGetFiles(unittest.TestCase):

    def test_get_parent(self):
        print(f"Result for \'../\' directory:")
        result = get_file_content("calculator", "main.py")
        print(result)

    def test_current(self):
        print(f"Result for current directory:")
        result = get_file_content("calculator", "pkg/calculator.py")
        print(result)

    def test_pkg(self):
        print(f"Result for \'pkg\' directory:")
        result = get_file_content("calculator", "/bin/cat")
        self.assertIn("Error:",result)

    def test_bin(self):
        print(f"Result for \'/bin\' directory:")
        result = get_file_content("calculator", "pkg/does_not_exist.py")
        self.assertIn("Error:",result)

if __name__ == "__main__":
    unittest.main()
