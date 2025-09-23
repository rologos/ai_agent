import unittest
from functions.write_file import write_file 

class TestGetFiles(unittest.TestCase):

    def test_1(self):
        result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(result)
        self.assertIn("28 characters written",result)

    def test_2(self):
        result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print(result)
        self.assertIn("26 characters written",result)

    def test_3(self):
        result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print(result)
        self.assertIn("Error:",result)


if __name__ == "__main__":
    unittest.main()
