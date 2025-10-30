import unittest
import os

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), "../mood_diary" , "2025-10-30.txt")

class TestCalculations(unittest.TestCase):

    def setUp(self):
       self.testfile = open(TESTDATA_FILENAME)
       self.testdata = self.testfile.read()

    def tearDown(self):
       self.testfile.close()

    def test_diary_entry_contains_My_name_is(self):
        key = "My name is"
        container = self.testdata
        # error message in case if test case got failed
        message = "'My name is' is not in diary entry"
        # assertIn() to check if key is in container
        self.assertIn(key, container, message)

if __name__ == "__main__":
    unittest.main()
