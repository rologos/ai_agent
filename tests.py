import unittest
from functions.get_files_info import get_files_info 

class TestGetFiles(unittest.TestCase):

    def test_1(self):
        result = get_files_info({'directory': '.'})
        print(result)

    def test_2(self):
        result = get_files_info({'directory': 'pkg'})
        print(result)

if __name__ == "__main__":
    unittest.main()
